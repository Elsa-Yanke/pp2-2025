
"""CREATE OR REPLACE PROCEDURE import_contacts_from_json(
    IN fromjsondata JSON,
    OUT invalid_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    p_item JSON;
    p_name TEXT;
    p_last_name TEXT;
    p_phone TEXT;
    contact_id INT;
    invalid_list TEXT[] := '{}';  -- временный список для хранения неверных номеров
BEGIN
    -- Перебираем каждый объект в JSON-массиве
    FOR p_item IN SELECT * FROM json_array_elements(fromjsondata)
    LOOP
        p_name := p_item->>'имя';
        p_last_name := p_item->>'фамилия';
        p_phone := p_item->>'номер';

        -- Проверяем: номер соответствует формату +7XXXXXXXXXX
        IF p_phone ~ '^\+7\d{10}$' THEN
            -- Добавляем контакт и получаем его id
            INSERT INTO contacts(first_name, last_name)
            VALUES (p_name, p_last_name)
            RETURNING id INTO contact_id;

            -- Добавляем телефонный номер
            INSERT INTO phone_numbers(contact_id, phone_number)
            VALUES (contact_id, p_phone);
        ELSE
            -- Добавляем в список неверных номеров
            invalid_list := array_append(invalid_list, p_phone);
        END IF;
    END LOOP;

    -- Возвращаем список неверных номеров
    invalid_phones := invalid_list;
END;
$$;
"""
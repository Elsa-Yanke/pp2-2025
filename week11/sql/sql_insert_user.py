"""CREATE OR REPLACE PROCEDURE insert_or_update_contact(
    IN p_first_name VARCHAR,
    IN p_last_name VARCHAR,
    IN p_phone_number VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    user_id INT;
BEGIN
    -- Пытаемся найти ID пользователя с таким именем и фамилией
    SELECT id 
    INTO user_id 
    FROM contacts 
    WHERE first_name = p_first_name AND last_name = p_last_name;

    -- Если пользователь найден
    IF FOUND THEN
        -- Обновляем номер телефона по его contact_id
        UPDATE phone_numbers 
        SET phone_number = p_phone_number 
        WHERE contact_id = user_id;
    ELSE
        -- Вставляем нового пользователя и сохраняем его ID
        INSERT INTO contacts (first_name, last_name) 
        VALUES (p_first_name, p_last_name) 
        RETURNING id INTO user_id;

        -- Вставляем номер телефона для нового пользователя
        INSERT INTO phone_numbers (phone_number, contact_id) 
        VALUES (p_phone_number, user_id);
    END IF;
END;
$$;
"""
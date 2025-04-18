"""
CREATE OR REPLACE PROCEDURE delete_user(
    IN p_first_name TEXT,
    IN p_last_name TEXT,
    OUT result TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Проверяем, существует ли такой пользователь
    IF EXISTS (
        SELECT 1 FROM contacts
        WHERE first_name = p_first_name AND last_name = p_last_name
    ) THEN
        -- Удаляем связанные номера телефона
        DELETE FROM phone_numbers
        WHERE contact_id IN (
            SELECT id FROM contacts
            WHERE first_name = p_first_name AND last_name = p_last_name
        );

        -- Удаляем сам контакт
        DELETE FROM contacts
        WHERE first_name = p_first_name AND last_name = p_last_name;

        result := 'Пользователь удален';
    ELSE
        result := 'Такой пользователь не найден';
    END IF;
END;
$$;
"""
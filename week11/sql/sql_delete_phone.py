"""CREATE OR REPLACE PROCEDURE delete_phone_if_exists(
    IN p_phone_number VARCHAR,
    OUT results TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phone_numbers WHERE phone_number = p_phone_number
    ) THEN
        DELETE FROM phone_numbers WHERE phone_number = p_phone_number;
        results := 'номер удален';
    ELSE
        results := 'номера нет';
    END IF;
END;
$$;
"""
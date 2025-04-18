"""CREATE OR REPLACE FUNCTION get_contacts_with_pagination(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE (
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.first_name, c.last_name, p.phone_number
    FROM contacts c
    JOIN phone_numbers p ON c.id = p.contact_id
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$;
"""
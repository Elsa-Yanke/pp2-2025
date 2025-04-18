""" CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT contacts.id, contacts.first_name, contacts.last_name
    FROM contacts
    WHERE contacts.first_name ILIKE '%' || pattern || '%'
       OR contacts.last_name ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION search_users(text)

SELECT * FROM search_users('На');

"""
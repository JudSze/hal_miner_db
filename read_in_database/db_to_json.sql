DO $$
DECLARE
    tbl RECORD;
    result JSONB := '{}';
    table_data JSONB;
BEGIN
    FOR tbl IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
          AND table_type = 'BASE TABLE'
    LOOP
        EXECUTE format(
            'SELECT COALESCE(jsonb_agg(t), ''[]''::jsonb) FROM public.%I t',
            tbl.table_name
        ) INTO table_data;

        result := jsonb_set(result, ARRAY[tbl.table_name], table_data, true);
    END LOOP;

    -- Print the full JSON as one line
    RAISE NOTICE '%', result::TEXT;
END $$;

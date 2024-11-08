CREATE OR REPLACE PROCEDURE remove_chemical_from_product(product_id INTEGER, chemical_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM public."Chemical_List"
    WHERE "Product_ID" = product_id AND "Chemical_ID" = chemical_id;
END;
$$;

CREATE OR REPLACE PROCEDURE add_chemical_from_product(product_id INTEGER, chemical_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO public."Chemical_List" ("Product_ID", "Chemical_ID")
    VALUES (product_id, chemical_id);
END;
$$;



CREATE OR REPLACE PROCEDURE display_company_products()
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT
            "Company"."Company_Name" AS company_name,
            "Product"."Product_Name" AS product_name,
            "Product"."Product_ID" AS product_id
        FROM
            public."Company"
        JOIN
            public."Product" ON "Company"."Company_ID" = "Product"."Company_ID"
        ORDER BY
            "Company"."Company_Name", "Product"."Product_Name"
    LOOP
        RAISE NOTICE 'Company: %, Product: %, Product ID: %',
            rec.company_name, rec.product_name, rec.product_id;
    END LOOP;
END;
$$;

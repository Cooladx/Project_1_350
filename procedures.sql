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

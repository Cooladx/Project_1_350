CREATE OR REPLACE FUNCTION get_products_with_chemical(chemical_id INTEGER)
RETURNS TABLE("Product_ID" INTEGER, "Product_Name" VARCHAR) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p."Product_ID", p."Product_Name"
    FROM public."Product" p
    JOIN public."Chemical_List" cl ON p."Product_ID" = cl."Product_ID"
    WHERE cl."Chemical_ID" = chemical_id;
END;
$$;

CREATE OR REPLACE FUNCTION get_chemical_name_by_product_id(product_id INTEGER)
RETURNS TEXT
AS $$
DECLARE
    chemical_name TEXT;
BEGIN
    SELECT c.Chemical_Name
    INTO chemical_name
    FROM public.Chemical_List cl
    JOIN public.Chemical c ON cl.Chemical_ID = c.Chemical_ID
    WHERE cl.Product_ID = product_id;

    RETURN chemical_name;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_company_products()
RETURNS TABLE (
    company_name VARCHAR,
    product_name VARCHAR,
    product_id INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        "Company"."Company_Name",
        "Product"."Product_Name",
        "Product"."Product_ID"
    FROM 
        public."Company"
    JOIN 
        public."Product" ON "Company"."Company_ID" = "Product"."Company_ID"
    ORDER BY 
        "Company"."Company_Name", "Product"."Product_Name";
END;
$$ LANGUAGE plpgsql;

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
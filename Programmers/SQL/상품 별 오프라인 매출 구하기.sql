SELECT P.PRODUCT_CODE, sum(O.SALES_AMOUNT * P.PRICE) as SALES
FROM OFFLINE_SALE O, PRODUCT P
WHERE O.PRODUCT_ID = P.PRODUCT_ID
GROUP BY O.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE
SELECT f.FLAVOR
FROM FIRST_HALF f, ICECREAM_INFO i
WHERE i.INGREDIENT_TYPE = "fruit_based" and f.TOTAL_ORDER > 3000 and i.FLAVOR = f.FLAVOR
ORDER BY f.TOTAL_ORDER DESC
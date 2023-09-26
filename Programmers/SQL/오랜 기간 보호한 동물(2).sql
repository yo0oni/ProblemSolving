SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_INS a, ANIMAL_OUTS o
WHERE a.ANIMAL_ID = o.ANIMAL_ID
ORDER BY DATEDIFF(o.DATETIME, a.DATETIME) DESC
LIMIT 2
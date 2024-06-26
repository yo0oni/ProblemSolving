SELECT u.USER_ID, u.NICKNAME,
    concat(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) AS "전체주소",
    concat(substring(u.TLNO from 1 for 3), "-", substring(u.TLNO from 4 for 4), "-", substring(u.TLNO from 8 for 4)) AS "전화번호"
FROM USED_GOODS_BOARD b, USED_GOODS_USER u
WHERE b.WRITER_ID = u.USER_ID
GROUP BY b.WRITER_ID
HAVING COUNT(b.BOARD_ID) >= 3
ORDER BY u.USER_ID DESC
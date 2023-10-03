SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d')
FROM BOOK
JOIN AUTHOR
ON AUTHOR.AUTHOR_ID = BOOK.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE
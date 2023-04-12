
CREATE or REPLACE FUNCTION get_course_id_by_email(email VARCHAR(30))
RETURNS TABLE(id INTEGER) AS
$BODY$
	SELECT id
	FROM user_student
	WHERE email=$1
$BODY$
LANGUAGE SQL;


SELECT * FROM get_course_id_by_email('spencer@microsoft.com')


SELECT * FROM user_student
# Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name,
COUNT(ex.student_id) AS attended_exams 
FROM students st
CROSS JOIN Subjects su
LEFT JOIN Examinations ex
ON st.student_id = ex.student_id And su.subject_name = ex.subject_name
GROUP BY st.student_id, su.subject_name, st.student_name
ORDER BY st.student_id

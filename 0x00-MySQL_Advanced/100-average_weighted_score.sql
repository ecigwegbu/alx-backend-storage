-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN my_user_id INT
)
BEGIN
CREATE TEMPORARY TABLE temptable AS
SELECT corrections.user_id AS U_ID, corrections.project_id,
	    corrections.score AS SC, projects.weight AS WT, corrections.score * projects.weight AS PROD
	    	FROM (corrections LEFT JOIN projects ON corrections.project_id=projects.id);
UPDATE users SET average_score = (SELECT (SUM(PROD) / SUM(WT))FROM temptable WHERE U_ID = my_user_id)
    where id = my_user_id;

END //

DELIMITER ;

-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
    BEGIN
    DECLARE user INT DEFAULT 1;

    CREATE TEMPORARY TABLE temptables AS
        SELECT corrections.user_id AS U_ID, corrections.project_id,
            corrections.score, projects.weight AS WT,
            corrections.score * projects.weight AS PROD
            FROM (corrections LEFT JOIN projects
            ON corrections.project_id=projects.id);

    SELECT COUNT(*) INTO user FROM users;

    WHILE user > 0 DO
        UPDATE users SET average_score = (SELECT (SUM(PROD) / SUM(WT))
            FROM temptables WHERE U_ID = user)
        WHERE id = user;
    SET user = user - 1;
    END WHILE;

END //

DELIMITER ;

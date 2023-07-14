-- Write a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store the average
-- score for a student. Note: An average score can be a decimal

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN my_user_id INT
)
    UPDATE users
        SET average_score =
	    (SELECT AVG(score) FROM corrections	WHERE user_id=my_user_id)
	    WHERE id=my_user_id;

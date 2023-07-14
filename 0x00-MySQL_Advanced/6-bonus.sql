-- Write a SQL script that creates a stored procedure AddBonus that adds a new
-- correction for a student.

-- Requirements:

-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an
-- existing users)
-- project_name, a new or already exists projects - if no projects.name found in
-- the table, you should create it
-- score, the score value for the correction
-- Context: Write code in SQL is a nice level up!

DELIMITER //

DROP PROCEDURE IF EXISTS AddBonus;

CREATE PROCEDURE AddBonus(
    IN my_user_id INT,
    IN my_project_name VARCHAR(255),
    IN my_score INT
)
BEGIN
    -- get test_project_id, if it exists
    SET @test_project_id = NULL;
    SELECT id INTO @test_project_id FROM projects
        WHERE name = my_project_name;
    -- update the corrections table, but first check project name exists
    IF (@test_project_id) THEN
        -- project name exists
        INSERT INTO corrections (user_id, project_id, score)
            VALUES (my_user_id, @test_project_id, my_score);
    ELSE
        -- project name does not exist, so update projects table
        INSERT INTO projects (name) VALUES (my_project_name);
        SET @test_project_id = LAST_INSERT_ID();
        -- then update corrections table
        INSERT INTO corrections (user_id, project_id, score)
            VALUES (my_user_id, @test_project_id, my_score);
    END IF;
END //

DELIMITER ;

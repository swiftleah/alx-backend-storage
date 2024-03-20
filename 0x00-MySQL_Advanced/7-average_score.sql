-- this script creates a stored procedure ComputeAverageScoreForUser
-- procedure computes and stores average for student. can be decimal
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE avgscore FLOAT;
	SET avgscore = (SELECT AVG(score) FROM corrections as C WHERE C.user_id=user_id);
	UPDATE users SET average_score = avgscore WHERE id=user_id;
END $$
DELIMITER ;

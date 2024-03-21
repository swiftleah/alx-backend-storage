-- creates stored procedure that computes and stores student average score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE weightedScore FLOAT;
	SET weightedScore = (SELECT SUM(score * weight) / SUM(weight)
                        FROM users AS U
                        JOIN corrections as C ON U.id=C.user_id
                        JOIN projects AS P ON C.project_id=P.id
                        WHERE U.id=user_id);
    UPDATE users SET average_score = weightedScore WHERE id=user_id;
END $$
DELIMITER ;

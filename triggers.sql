DELIMITER //

CREATE TRIGGER before_employee_clock_in
BEFORE INSERT ON Attendance
FOR EACH ROW
BEGIN
    DECLARE existing_attendance INT;
    
    -- Check if there is an existing attendance entry for the employee with no clock-out time
    SELECT COUNT(*)
    INTO existing_attendance
    FROM Attendance
    WHERE EmployeeID = NEW.EmployeeID AND ClockOut IS NULL;
    
    -- If an existing entry with no clock-out time is found, prevent the new clock-in entry
    IF existing_attendance > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Employee has an active attendance entry. Clock out first.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER before_employee_clock_out
BEFORE UPDATE ON Attendance
FOR EACH ROW
BEGIN
    DECLARE existing_attendance INT;
    
    -- Check if there is an existing clock-in entry for the employee
    SELECT COUNT(*)
    INTO existing_attendance
    FROM Attendance
    WHERE EmployeeID = NEW.EmployeeID AND ClockOut IS NULL;
    
    -- If no clock-in entry is found, prevent the new clock-out entry
    IF existing_attendance = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Employee must clock in before clocking out.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER InsertNotificationAfterEmployeeShift1
AFTER INSERT ON EmployeeShift
FOR EACH ROW
BEGIN
    DECLARE shift_date DATE;
    DECLARE shift_type VARCHAR(255);
    DECLARE notif_message VARCHAR(255);

    -- Retrieve the shift date and type for the newly inserted row
    SELECT NEW.shiftDate, NEW.shiftType INTO shift_date, shift_type;

    -- Prepare the notification message
    SET notif_message = CONCAT('You have been assigned a shift on ', shift_date, ', ', shift_type);

    -- Insert the notification into the Notification table
    INSERT INTO Notification (EmployeeID, Notif)
    VALUES (NEW.EmployeeID, notif_message);
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER UpdateNotificationAfterEmployeeShift
AFTER UPDATE ON EmployeeShift
FOR EACH ROW
BEGIN
    DECLARE shift_date DATE;
    DECLARE shift_type VARCHAR(255);
    DECLARE notif_message VARCHAR(255);

    -- Check if EmployeeID has been updated
    IF OLD.EmployeeID <> NEW.EmployeeID THEN
        -- Retrieve the shift date and type for the updated row
        SELECT NEW.shiftDate, NEW.shiftType INTO shift_date, shift_type;

        -- Prepare the notification message
        SET notif_message = CONCAT('You have been assigned a shift on ', shift_date, ', ', shift_type);

        -- Insert the notification into the Notification table
        INSERT INTO Notification (EmployeeID, Notif)
        VALUES (NEW.EmployeeID, notif_message);
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER InsertNotificationAfterEmployeeLeave2
AFTER UPDATE ON EmployeeLeave
FOR EACH ROW
BEGIN
    DECLARE notif_message VARCHAR(255);

    -- Determine the outcome of the leave
    IF NEW.status = 'Approved' THEN
        SET notif_message = CONCAT('Your leave on ', NEW.Date, ' has been approved.');
    ELSEIF NEW.status = 'Rejected' THEN
        SET notif_message = CONCAT('Your leave on ', NEW.Date, ' has been rejected.');
    END IF;

    -- Insert the notification into the Notification table
    INSERT INTO Notification (EmployeeID, Notif)
    VALUES (NEW.EmployeeID, notif_message);
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER InsertIntoApprovedEmployeeLeave
AFTER UPDATE ON EmployeeLeave
FOR EACH ROW
BEGIN
    -- Check if the leave status is 'Approved'
    IF NEW.status = 'Approved' THEN
        -- Insert the corresponding record into the ApprovedEmployeeLeave table
        INSERT INTO ApprovedEmployeeLeave (EmployeeID, Date, LeaveType, status)
        VALUES (NEW.EmployeeID, NEW.Date, NEW.LeaveType, NEW.status);
    END IF;
END;
//

DELIMITER ;

SELECT CONCAT('DROP TRIGGER IF EXISTS ', trigger_name, ';')
FROM information_schema.triggers
WHERE trigger_schema = 'FYP';
DROP TRIGGER IF EXISTS InsertNotificationAfterEmployeeShift;
DROP TRIGGER IF EXISTS UpdateNotificationAfterEmployeeShift;
DROP TRIGGER IF EXISTS InsertNotificationAfterEmployeeLeave;
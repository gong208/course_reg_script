# course_reg_script
a simple script for registering courses at UIUC using selenium.
It refreshes course explorer every 30 sec to monitor the status of CS222. Once it is not in closed status (there are spaces), it logs in to the self-service course registration system with the account and password provided and attempts to register for a class. If the registered hours increase, which means the course is successfully registered, the program ends. Otherwise, it goes back to Course Explorer and continues to listen to the status of the course.

Because of the existence of Duo authentication, you'll have to approve the authentication manually.
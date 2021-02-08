#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Runs forever
 * Return: Nothing
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Where the program starts
 * Return: Always 0
 */

int main(void)
{
	int i;
	int child_PID;

	for (i = 0; i < 5; i++)
	{
		child_PID = fork();
		if (child_PID > 0)
			printf("Zombie process created, PID: %d\n", child_PID);
		else
			exit(0);
	}

	infinite_while();

	return (0);
}

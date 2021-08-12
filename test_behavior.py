import pytest

class JobRunner:
    def run(self, job_name):
        message = f"Running job {job_name}"
        self.log(message)

    def run_with_check(self, job_name):
        if job_name == 'NONEXSITENT_JOB':
            self.log('Error: Job not found!')

    def log(self, message):
        print(f"Log: {message}")


def test_if_job_is_logged(mocker):
    m = mocker.patch.object(JobRunner, 'log')
    runner = JobRunner()
    runner.run("test_job")
    m.assert_called_once()


def test_if_error_is_logged(mocker):
    m = mocker.patch.object(JobRunner, 'log')
    runner = JobRunner()
    runner.run_with_check('NONEXSITENT_JOB')
    m.assert_called_once_with('Error: Job not found!')

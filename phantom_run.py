# phantom_run.py
from modules import ai_helper, logger, system_reporter

def main():
    code = "for i in range(10): print(i)"
    suggestion = ai_helper.get_code_suggestion(code)
    report = system_reporter.get_system_report()

    logger.log_event("Running phantom_run")
    logger.log_event(f"AI Suggestion: {suggestion}")
    logger.log_event(f"System Report: {report}")

    print("AI Suggestion:", suggestion)
    print("System Report:", report)

if __name__ == "__main__":
    main()

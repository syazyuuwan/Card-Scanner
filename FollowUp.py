class FollowUp:
    course_dict = {
        "Course Name":"Target Audience",
        "AI in Business Automation Workflow":"Business professionals with an MBA or equivalent, Individuals interested in business strategy, Those seeking to improve business operations, Learners with no prior AI knowledge",
        "AI Application Design":"Graduates in computer science, engineering, IT and any talents that have basic knowledge on Python",
        "AI for Executives":"business leaders, managers, consultants, advisors, entrepeneurs, knowledge workers across all levels",
        "AI and Langchain Application":"Software Developers,Academic Researchers,Product Managers",
        "AI in Management":"Cross-industry collaboration fosters the establishment of AI networks, enabling individuals to become AI leaders within their organisations, driving the application of artificial intelligence forward.",
        "AI and Data Analytics with Low Code":"Project Managers,Marketing or Financial Analyst,Business Intelligence Developers,Operations Analysts,Project or IT Engineers",
        "AI and Data Science with Low Code":"Data Scientists,Marketing or Financial Analyst,Business Intelligence Developers,Operations Analysts,Project or IT Engineers",
        "AI for Creative Marketing":"Graduates in business, marketing, and anyone that is interested in expanding their knowledge and skills in digital marketing, particularly with the integration of AI technologies."
    }
    
    def email_draft(name): 
        draft = f"""
            Hello {name}!

            [[Generate a short thank you message]]

            Base on AI analysis of your profile, here are some suitable courses for you:
            [[Numbered list of course names]]

            Disclaimer: The contents of this email was AI generated
            """
        return draft
    
    def email_prompt(pos, com_name, com_vertical, name, course_dict):
        prompt = f"""You are a business development associate for AI Nusantara and writing an email to follow up potential leads who are visiting your exhibition booth at National Training Week.
                    You are writing lead conversion emails to reach out to a {pos} from {com_name} who are in the {com_vertical} industry. 
                    Fill in the contents that are denoted using double square brackets AKA [[]].
                    Write the email body only
                    Analyse their info and this dictionary {course_dict}, and suggest suitable courses. 
                    Use the following template:
                    {FollowUp.email_draft(name)}"""
        return prompt
    
    
from crewai import Crew, Agent, Task
from utils.file_loader import read_pdf
from utils.embedding_store import create_vector_store
from agents.credential_checker_agent import find_credentials
from agents.login_agent import guess_platform, simulate_login

# Step 1: Read PDF
text = read_pdf("data/example.pdf")

# Step 2: Store in Vector DB
chunks = text.split("\n\n")
vector_store = create_vector_store(chunks)

# Step 3: Find credentials
emails, phones, passwords = find_credentials(text)

# Step 4: Use CrewAI
reader = Agent(name="Reader Agent", role="Reader", goal="Extract text from PDF")
checker = Agent(name="Checker Agent", role="Credential Checker", goal="Check for missing credentials")
login = Agent(name="Login Agent", role="Login Manager", goal="Login to identified platform")

task = Task(description="Read file, check for credentials, identify platform, and simulate login.", agent=reader)
crew = Crew(agents=[reader, checker, login], tasks=[task])

crew.kickoff()

# Fallback: if missing details, ask user
if not passwords:
    passwords = [input("Enter password: ")]
if not emails and not phones:
    emails = [input("Enter email: ")]

platform = guess_platform(text)
simulate_login(platform, emails[0], passwords[0])

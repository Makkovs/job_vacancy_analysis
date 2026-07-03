import os
import json
import random

directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(directory, "config.json")

with open(path, "r", encoding="utf-8") as f:
    config = json.load(f)

def generate_job ():
    experience = random.choices(list(range(9)), config["EXPERIENCE_WEIGHTS"])[0]
    
    countries_config = config["COUNTRIES_CONFIG"]
    countries_list = list(countries_config.keys())
    countries_weights = [country["weight"] for country in countries_config.values()]
    country = random.choices(countries_list, countries_weights)[0]
    country_salary_coef = countries_config[country]["salary_coef"]
    
    domains_config = config["DOMAINS_CONFIG"]
    domains_list = list(domains_config.keys())
    domains_weights = [domain["weight"] for domain in domains_config.values()]
    domain = random.choices(domains_list, domains_weights)[0]

    domain_data = domains_config[domain]
    salary_base = domain_data["salary_base"]
    qualification = random.choices([0, 1, 2, 3], domain_data["qualification_weights"])[0]

    main_skills_config = config["MAIN_SKILLS_CONFIG"][domain]
    main_skills_list = list(main_skills_config.keys())
    main_skills_weights = [skill["weight"] for skill in main_skills_config.values()]
    main_skill = random.choices(main_skills_list, main_skills_weights)[0]
    skills = main_skills_config[main_skill]["skills"].copy()
    salary_bonus = main_skills_config[main_skill]["salary_bonus"]

    utils_bonus = 0
    for skill, probability in config["UTIL_SKILLS"].items():
        if random.random() + 0.015 * experience < probability:
            utils_bonus += random.choice([0, 100])
            skills.append(skill)

    base = salary_base * country_salary_coef * (1 + 0.25 * experience) * (1 + 0.1 * qualification)
    salary = int(base + random.uniform(0.5, 1.8) * salary_bonus + utils_bonus)
    
    job = {
        "title" : f"{["Junior", "Middle", "Senior"][round(experience/4)]} {domain} {main_skill} developer",
        "salary_min" : int(salary*0.8),
        "salary_max" : int(salary*1.2),
        "experience" : experience,
        "country" : country,
        "skills" : skills
    }
    
    return job
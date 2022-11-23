import datetime
import json

from sqlalchemy import Column, Integer, String, DateTime, create_engine, Float, ForeignKey, Text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from api.fullstack_challenge_api.models.Company import Company, Base
from api.fullstack_challenge_api.models.Deal import Deal


def load_companies_and_deals_from_files(user, password, url, db_name, company_file, deals_file):
    uri = f"mysql+pymysql://{user}:{password}@{url}/{db_name}"

    engine = create_engine(uri)
    Session = sessionmaker(engine)

    companies_parsed = json.load(open(company_file))

    company_ids = set()
    companies = []
    for company_data in companies_parsed.values():
        founding_date = None if company_data['founding_date'] is None \
            else datetime.datetime.strptime(company_data['founding_date'], '%Y-%m-%dT%H:%M:%SZ')
        company = Company(company_id=company_data['company_id'],
                          name=company_data['name'],
                          country=company_data['country'],
                          founding_date=founding_date,
                          description=company_data['description'])
        company_ids.add(company.company_id)
        companies.append(company)

    deals_parsed = json.load(open(deals_file))
    deals = []
    for deal_data in deals_parsed.values():
        if not company_ids.__contains__(deal_data['company_id']):
            continue
        date = None if deal_data['date'] is None \
            else datetime.datetime.fromtimestamp(deal_data['date'] / 1e3)
        deal = Deal(date=date,
                    funding_amount=deal_data['funding_amount'],
                    funding_round=deal_data['funding_round'],
                    company_id=deal_data['company_id'])
        deals.append(deal)

    Base.metadata.create_all(engine)
    with Session() as session:
        session.add_all(companies)
        session.add_all(deals)
        session.commit()


if __name__ == 'main':
    company_file = '../../../data/challenge_companies.json'
    deals_file = '../../../data/challenge_deals.json'
    load_companies_and_deals_from_files('user', 'pw', 'host', 'db', company_file,
                                        deals_file)

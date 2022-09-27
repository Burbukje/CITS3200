from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification


def  db_add_possible_classification(classification, headers: list,matched) -> None:

    classification_name = matched
    classification.possible_classifications = classification_name
    classification.save()



mysqldump -u root --skip-add-drop-table --no-create-info medline  models_medline_citation_authors__models_medline_author_citations models_medline_citation_languages__models_medline_language models_medline_citation_pub_types__models_medline_pubtype pub_type_citation lan_cit models_medline_subheadingterm models_medline_citation_meshterms__models_medline_termcitation  models_medline_termcitation models_medline_citation > citations.sql
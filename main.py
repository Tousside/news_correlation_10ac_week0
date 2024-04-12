def tf_idf_similarity(title, body):
  # cobine title and body in a list
  title_body=[title, body]

  # Create an instance of  TfidfVectorizer
  vectorizer = TfidfVectorizer()
  # get tf-idf scores
  tfidf_matrix = vectorizer.fit_transform(title_body)
  # title and body similarity score
  similarity_scores = cosine_similarity( tfidf_matrix , tfidf_matrix)
  return similarity_scores[0,1]

if __name__=="__tf_idf_similarty__":
    title="superstar chef yannick alléno brings refined french cuisine pavyllon london"
    body= "avyllon london four seasons hotel london park lane one worlds best chefs\
    created new culinary stage london yannick alléno superstar french chef \
    nabbed impressive 15 michelin stars recently made uk debut opening pavyllon\
    london located four seasons hotel london park lane fashionable mayfair\
    new restaurant showcases allénos modern"
    tf_idf_similarity(title, body)
CREATE TABLE "domains_location" (
  "source_common_name" varchar PRIMARY KEY,
  "location" varchar,
  "country" varchar
);

CREATE TABLE "articles" (
  "article_id" integer PRIMARY KEY,
  "source_name" varchar,
  "title" varchar,
  "content" varchar,
  "published_at" timestamp
);

CREATE TABLE "traffic" (
  "domain" varchar PRIMARY KEY,
  "global_rank" integer
);

ALTER TABLE "articles" ADD FOREIGN KEY ("source_name") REFERENCES "domains_location" ("source_common_name");

ALTER TABLE "traffic" ADD FOREIGN KEY ("domain") REFERENCES "domains_location" ("source_common_name");

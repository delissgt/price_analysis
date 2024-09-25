CREATE TABLE products
(
    "id"                uuid    NOT NULL DEFAULT uuid_generate_v4(),
    "name"              varchar            DEFAULT ''::character varying,
    "brand"             varchar            DEFAULT ''::character varying,
    "full_price"        varchar            DEFAULT ''::character varying,
    "discount_price"    float              DEFAULT 0.0,
    "in_stock"          bool               DEFAULT false,
    "url"               varchar            DEFAULT ''::character varying,
    "url_img"           varchar            DEFAULT ''::character varying,
    PRIMARY KEY ("id")
);
CREATE TABLE products
(
    "id"                uuid    NOT NULL DEFAULT uuid_generate_v4(),
    "name"              varchar            DEFAULT ''::character varying,
    "ean"               int                DEFAULT 0,
    "brand"             varchar            DEFAULT ''::character varying,
    "full_price"        float              DEFAULT 0.0,
    "discount_price"    float              DEFAULT 0.0,
    "in_stock"          bool               DEFAULT false,
    "url"               varchar            DEFAULT ''::character varying,
    "url_img"           varchar            DEFAULT ''::character varying,
    PRIMARY KEY ("id")
);
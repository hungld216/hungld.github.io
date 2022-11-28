from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    total = fields.Int(required=True)
    price = fields.Float(required=True)
    date_exprired = fields.Str(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    address = fields.Str()
    total = fields.Int()


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    staff = fields.Int()
    address = fields.Str()
    phone = fields.Int()
    user = fields.Str()
    password = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    user = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    id = fields.Int()
    total = fields.Int()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)


class TagSchema(PlainUserSchema):
    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

# API review checklist

## Resource model
- [ ] Resources are nouns, actions are verbs against them
- [ ] Naming consistent with neighboring APIs
- [ ] Plural for collections, singular for items
- [ ] Hierarchy reflects ownership, not happenstance

## Operations
- [ ] CRUD verbs match HTTP semantics (GraphQL: query vs mutation)
- [ ] Idempotency keys on POSTs that create
- [ ] Bulk endpoints when N is realistic

## Inputs
- [ ] Required vs optional fields documented
- [ ] Validation rules (length, format, enum) explicit
- [ ] Defaults documented

## Outputs
- [ ] Stable shape; additive evolution preferred
- [ ] Errors typed (code + message) and enumerable
- [ ] Empty / "not found" states documented

## Pagination
- [ ] All list endpoints paginate
- [ ] Cursor preferred over offset for changing data
- [ ] Page size capped

## Auth
- [ ] Auth model documented
- [ ] AuthZ rules per operation (who can call?)
- [ ] Rate limits documented (or pointer to global doc)

## Errors
- [ ] 4xx vs 5xx semantics correct
- [ ] Error body shape consistent across endpoints
- [ ] No internal stack traces leak

## Compatibility
- [ ] Breaking changes flagged + migration plan
- [ ] Versioning strategy explicit
- [ ] Deprecations have a sunset date

## Observability
- [ ] Tracing identifiers preserved
- [ ] Log fields documented for sensitive data redaction



CREATE TABLE "Annotation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, object)
);

CREATE TABLE "Assertion" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement)
);

CREATE TABLE "AttributedName" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"namingAuthority" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "namingAuthority")
);

CREATE TABLE "Bag" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Bundle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "CoItem" (
	"itemOf" TEXT, 
	PRIMARY KEY ("itemOf")
);

CREATE TABLE "Collection" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Compilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ConfidenceFacet" (
	confidence INTEGER NOT NULL, 
	PRIMARY KEY (confidence)
);

CREATE TABLE "ContextualCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ControlledDictionary" (
	entry TEXT, 
	PRIMARY KEY (entry)
);

CREATE TABLE "ControlledDictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "ControlledVocabulary" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"constrainingVocabularyReference" TEXT, 
	"constrainingVocabularyName" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "constrainingVocabularyReference", "constrainingVocabularyName", value)
);

CREATE TABLE "Dictionary" (
	entry TEXT NOT NULL, 
	PRIMARY KEY (entry)
);

CREATE TABLE "DictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "EnclosingCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ExternalReference" (
	"referenceURL" TEXT, 
	"definingContext" TEXT, 
	"externalIdentifier" TEXT, 
	PRIMARY KEY ("referenceURL", "definingContext", "externalIdentifier")
);

CREATE TABLE "Grouping" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	context TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object, context)
);

CREATE TABLE "Hash" (
	"hashValue" TEXT NOT NULL, 
	"hashMethod" TEXT NOT NULL, 
	PRIMARY KEY ("hashValue", "hashMethod")
);

CREATE TABLE "IdentityAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Item" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "List" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	"lastItem" TEXT, 
	"firstItem" TEXT, 
	PRIMARY KEY (element, size, item, "lastItem", "firstItem")
);

CREATE TABLE "ListItem" (
	"itemOf" TEXT, 
	_index INTEGER NOT NULL, 
	PRIMARY KEY ("itemOf", _index)
);

CREATE TABLE "MarkingDefinitionAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ModusOperandi" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Relationship" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"endTime" DATETIME, 
	"isDirectional" BOOLEAN NOT NULL, 
	"kindOfRelationship" TEXT, 
	source TEXT NOT NULL, 
	"startTime" DATETIME, 
	target TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "endTime", "isDirectional", "kindOfRelationship", source, "startTime", target)
);

CREATE TABLE "Set" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Thread" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	PRIMARY KEY (element, size, item)
);

CREATE TABLE "ThreadItem" (
	"itemContent" TEXT, 
	PRIMARY KEY ("itemContent")
);

CREATE TABLE "UcoObject" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

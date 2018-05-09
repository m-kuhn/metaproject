=========================================
Meta Attributes
=========================================

.. contents::


General
================

	«To a metaelement metaattributes could be compositional assigned (class "MetaAttribut"). The metaattributes are neither defined by the language INTERLIS nor by the meta model. They exist that the information that exceed INTERLIS could still be a component of the model data. The metaattributes has a name (attribute "Name"), that have to be unique among the the metaattributes of this metaelement, and it has a value (attribute: "Value").»

Translated from source: `STAN_d_DEF_2011-06-22_eCH-0117 Meta-Attribute für INTERLIS-Modelle.pdf 
<https://www.ech.ch/alfresco/s/ech/download?nodeid=788eb38a-bf2b-4f3d-96a8-addc37bba41f>`_ (German) from eCH www.interlis.ch

Meta Attributes in Interlis Files
------------------------------------------

**Comment vs. Attribute**

An Interlis comment starts with ``!!`` and ends with a line end. An attribute starts with ``!!`` as well but followed by an ``@``:

**Syntax**

After the start of ``!!@`` the attribute name follows, then equal, then the attribute value:

::

	!!@<name>=<value>

Followed by the referenced element (MODEL, TOPIC, CLASS etc.)

**Example**

::

	!!@ furtherInformation=https://www.astra.admin.ch/
	MODEL ExceptionalLoadsCatalogues_V1 (en)
	AT "http://models.geo.admin.ch/ASTRA/"
	VERSION "2017-02-08"  =
	  IMPORTS CatalogueObjects_V1,Units;
	  !!@ topicInformation="Route-Type"
	  TOPIC TypeOfRouteCatalogue
	  EXTENDS CatalogueObjects_V1.Catalogues =
	    !!@ dispExpression="CONCAT(type, ' sometext')"
	    CLASS TypeOfRoute
	    EXTENDS CatalogueObjects_V1.Catalogues.Item =

``furtherInformation`` is referenced to ``ExceptionalLoadsCatalogues_V1``, ``topicInformation`` to ``TypeOfRouteCatalogue`` and ``dispExpression`` to ``TypeOfRoute``.

For more complex usage see the `specification of the Verein eCH <https://www.ech.ch/alfresco/s/ech/download?nodeid=788eb38a-bf2b-4f3d-96a8-addc37bba41f>`_

Meta Attributes in the Database
------------------------------------------

When importing the data from the Interlis file to the DB, with ili2db integrated in the Project Generator, the meta attributes are stored in the table **t_ili2db_meta_attrs**:

===============================================================  ==================  ===========================
ilielement                                                       attr_name           attr_value
===============================================================  ==================  ===========================
ExceptionalLoadsCatalogues_V1                                    furtherInformation  https://www.astra.admin.ch/
ExceptionalLoadsCatalogues_V1.TypeOfRouteCatalogue               topicInformation    Route-Type
ExceptionalLoadsCatalogues_V1.TypeOfRouteCatalogue.TypeOfRoute   dispExpression      CONCAT(type, ' sometext')
===============================================================  ==================  ===========================


Project Generator Specific Attributes
================================================

Some additional non standard meta attributes are understood by the project generator as properties in the QGIS project.

List of specific Attributes
------------------------------------------

**dispExpression**
Used as the display expression of a Relation Reference Widget. 

|relation_reference|


Extra Model Information File
================================

In these external files the meta attributes can be stored instead of having them directly in the Interlis files. 

These files are written in TOML and have the filename extension ``.toml``

You can select the extra meta attribute files in the **Advanced Options**. This configuration is stored for the model. Means when you reselect the model later again, the file is still referenced. This information will be displayed on the main dialog of the Project Generator.

In the background ili2pg writes the attributes from the external meta attribute file to the PostGIS or GeoPackage storage, where the Project Generator can use them to build the QGIS project.

**Example**
::

	["ExceptionalLoadsCatalogues_V1.TypeOfRouteCatalogue.TypeOfRoute"]
	dispExpression="CONCAT(type, ' sometext')"

**More simple example**
::

	["ExceptionalLoadsRoute.TypeOfRouteCatalogue.TypeOfRoute"]
	dispExpression="type"

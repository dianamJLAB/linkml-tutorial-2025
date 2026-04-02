-- # Class: NaradModel Description: Top-level NARAD document container.
--     * Slot: id
--     * Slot: narad_id
-- # Class: NaradConfig Description: NARAD configuration block containing the capability layer.
--     * Slot: id
--     * Slot: schema_version
--     * Slot: intent
--     * Slot: facility
--     * Slot: control_system
--     * Slot: capability_layer_id
--     * Slot: signal_layer_id Description: Signal-layer container for facility-specific signal bindings.
-- # Class: CapabilityLayer Description: Capability-layer container for profile families.
--     * Slot: id
-- # Class: SignalLayer Description: Signal-layer container for facility-specific signal bindings.
--     * Slot: id
-- # Class: Facility Description: A facility with specific signal bindings.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: control_system
--     * Slot: naming_convention
--     * Slot: SignalLayer_id Description: Autocreated FK slot
--     * Slot: signal_definitions_id
-- # Class: SignalDefinitions Description: Grouped EPICS signal suffix templates by semantic category.
--     * Slot: id
-- # Class: SignalBinding Description: A named EPICS suffix definition for one semantic signal.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: epics_suffix Description: Facility-specific EPICS suffix for a semantic signal.
--     * Slot: description
--     * Slot: SignalDefinitions_id Description: Autocreated FK slot
--     * Slot: DeviceTypeSignalSet_name Description: Autocreated FK slot
-- # Class: DeviceTypeSignalSet Description: Signal binding set scoped to a device type (for example, Quadrupole or BPM).
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: SignalDefinitions_id Description: Autocreated FK slot
-- # Class: Signal Description: A named semantic signal used by a capability.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: role Description: The role of the signal in the control model.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Units of measurement or null for unitless values.
--     * Slot: description
--     * Slot: Capability_name Description: Autocreated FK slot
--     * Slot: TypeSpecificCapability_id Description: Autocreated FK slot
-- # Class: Capability Description: A grouping of related signals for a control aspect.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: description
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: TypeSpecificCapability Description: An inline capability declared within a device-type profile, with its own identifier, a semantic class label, a description, and a list of signals. Distinct from the shared capabilities referenced by name; these are profile-local definitions.
--     * Slot: id Description: Unique identifier for the entity.
--     * Slot: capability_class Description: Semantic class label for a type-specific capability (e.g. QuadrupoleStrengthCapability). Serialized as 'class' in source YAML; renamed here to avoid conflict with reserved keywords.
--     * Slot: description
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
-- # Class: CapabilityProfile Description: A device-type profile that reuses shared capabilities and adds specific capabilities.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: kind Description: Kind/type of the profile family or profile instance.
--     * Slot: description
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: NodeLabels Description: Labels used when projecting the profile model into a graph view.
--     * Slot: id
--     * Slot: device
--     * Slot: capability_family
--     * Slot: profile
--     * Slot: capability
--     * Slot: signal
-- # Class: GraphProjection Description: Graph projection metadata for node labels and edge categories.
--     * Slot: id
--     * Slot: node_labels_id Description: Node label mapping for the graph projection.
-- # Class: ControlProfileFamily Description: A reusable family of control profiles sharing common semantics and structure.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: kind Description: Kind/type of the profile family or profile instance.
--     * Slot: description
--     * Slot: CapabilityLayer_id Description: Autocreated FK slot
--     * Slot: graph_projection_id Description: Optional graph projection metadata attached to a profile family.
-- # Class: Beamline Description: An ordered sequence of beamline elements defining a beam path.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: kind Description: Kind/type of the profile family or profile instance.
--     * Slot: NaradModel_id Description: Autocreated FK slot
-- # Class: BeamlineElement Description: A single element in a beamline with optional physics parameter blocks.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: kind Description: Kind/type of the profile family or profile instance.
--     * Slot: length Description: Physical length of the element in meters.
--     * Slot: NaradModel_id Description: Autocreated FK slot
--     * Slot: RFP_id Description: RF cavity physics parameters block.
--     * Slot: BendP_id Description: Dipole/bend physics parameters block.
--     * Slot: MagneticMultipoleP_id Description: Magnetic multipole physics parameters block.
--     * Slot: SolenoidP_id Description: Solenoid physics parameters block.
--     * Slot: narad_id
--     * Slot: JLabP_id Description: JLab-specific element parameters block.
-- # Class: ElementNaradRef Description: NARAD semantic reference block attached to a beamline element.
--     * Slot: id
--     * Slot: capability_profile_family Description: Cross-reference to the control profile family for this element.
--     * Slot: capability_profile Description: Cross-reference to the specific capability profile applied to this element.
--     * Slot: magnet_semantics_id Description: Magnet-domain semantic context for this element.
--     * Slot: instrument_semantics_id Description: Instrument-domain semantic context for this element.
--     * Slot: cavity_semantics_id Description: RF-cavity-domain semantic context for this element.
-- # Class: ElementSemantics Description: Semantic context referencing shared and type-specific capability names for a beamline element.
--     * Slot: id
-- # Class: PVBinding Description: A concrete PV (Process Variable) binding for one semantic signal on a beamline element.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: facility
--     * Slot: control_system
--     * Slot: pv Description: The EPICS Process Variable name (e.g. MBHK101H.S).
--     * Slot: ElementNaradRef_id Description: Autocreated FK slot
-- # Class: RFParams Description: RF cavity physics parameters (frequency, voltage, phase).
--     * Slot: id
--     * Slot: frequency Description: RF frequency in Hz.
--     * Slot: voltage Description: RF voltage in volts.
--     * Slot: phase Description: RF phase in degrees.
-- # Class: BendParams Description: Dipole/bend physics parameters (entry angle, exit edge angles).
--     * Slot: id
--     * Slot: angle_ref Description: Reference bend angle in radians.
--     * Slot: e1 Description: Entry edge angle in radians.
--     * Slot: e2 Description: Exit edge angle in radians.
-- # Class: MagneticMultipoleParams Description: Magnetic multipole physics parameters.
--     * Slot: id
--     * Slot: kn1 Description: First-order magnetic multipole coefficient (quadrupole strength).
-- # Class: SolenoidParams Description: Solenoid physics parameters.
--     * Slot: id
--     * Slot: ksol Description: Solenoid integrated field strength.
-- # Class: JLabParams Description: JLab-specific element parameters: type designation, accelerator model name, and open property map.
--     * Slot: id
--     * Slot: jlab_type Description: JLab-specific element type designation (e.g. WarmCavity, QW, HCorrector). Serialized as 'type' in source YAML; renamed here to avoid conflict with the LinkML metamodel 'type' designator used for polymorphic class selection.
--     * Slot: modeled_as Description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
-- # Class: KeyValuePair Description: A generic key-value pair for open-ended property maps.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: value Description: Property value as a string.
--     * Slot: JLabParams_id Description: Autocreated FK slot
-- # Class: CapabilityProfile_inherits_shared_capabilities
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
--     * Slot: inherits_shared_capabilities Description: Names of shared capabilities inherited by the profile.
-- # Class: GraphProjection_relationships
--     * Slot: GraphProjection_id Description: Autocreated FK slot
--     * Slot: relationships Description: Relationship labels used in graph projection.
-- # Class: Beamline_line
--     * Slot: Beamline_name Description: Autocreated FK slot
--     * Slot: line_name Description: Ordered sequence of cross-referenced element names forming a beamline.
-- # Class: ElementSemantics_shared_capabilities
--     * Slot: ElementSemantics_id Description: Autocreated FK slot
--     * Slot: shared_capabilities_name Description: Names of shared capabilities applied to this element, referencing Capability by name.
-- # Class: ElementSemantics_type_specific_capabilities
--     * Slot: ElementSemantics_id Description: Autocreated FK slot
--     * Slot: type_specific_capabilities_id Description: Capability class labels (e.g. CorrectorKickCapability) identifying which type-specific capabilities apply to this element. These match the capability_class field of TypeSpecificCapability entries in the profile.

CREATE TABLE "CapabilityLayer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CapabilityLayer_id" ON "CapabilityLayer" (id);
CREATE TABLE "SignalLayer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalLayer_id" ON "SignalLayer" (id);
CREATE TABLE "SignalDefinitions" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalDefinitions_id" ON "SignalDefinitions" (id);
CREATE TABLE "NodeLabels" (
	id INTEGER NOT NULL,
	device TEXT,
	capability_family TEXT,
	profile TEXT,
	capability TEXT,
	signal TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NodeLabels_id" ON "NodeLabels" (id);
CREATE TABLE "ElementSemantics" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ElementSemantics_id" ON "ElementSemantics" (id);
CREATE TABLE "RFParams" (
	id INTEGER NOT NULL,
	frequency FLOAT,
	voltage FLOAT,
	phase FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RFParams_id" ON "RFParams" (id);
CREATE TABLE "BendParams" (
	id INTEGER NOT NULL,
	angle_ref FLOAT,
	e1 FLOAT,
	e2 FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BendParams_id" ON "BendParams" (id);
CREATE TABLE "MagneticMultipoleParams" (
	id INTEGER NOT NULL,
	kn1 FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MagneticMultipoleParams_id" ON "MagneticMultipoleParams" (id);
CREATE TABLE "SolenoidParams" (
	id INTEGER NOT NULL,
	ksol FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SolenoidParams_id" ON "SolenoidParams" (id);
CREATE TABLE "JLabParams" (
	id INTEGER NOT NULL,
	jlab_type TEXT,
	modeled_as TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_JLabParams_id" ON "JLabParams" (id);
CREATE TABLE "NaradConfig" (
	id INTEGER NOT NULL,
	schema_version TEXT,
	intent TEXT,
	facility TEXT,
	control_system TEXT,
	capability_layer_id INTEGER,
	signal_layer_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(capability_layer_id) REFERENCES "CapabilityLayer" (id),
	FOREIGN KEY(signal_layer_id) REFERENCES "SignalLayer" (id)
);CREATE INDEX "ix_NaradConfig_id" ON "NaradConfig" (id);
CREATE TABLE "Facility" (
	name TEXT NOT NULL,
	control_system TEXT,
	naming_convention TEXT,
	"SignalLayer_id" INTEGER,
	signal_definitions_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalLayer_id") REFERENCES "SignalLayer" (id),
	FOREIGN KEY(signal_definitions_id) REFERENCES "SignalDefinitions" (id)
);CREATE INDEX "ix_Facility_name" ON "Facility" (name);
CREATE TABLE "DeviceTypeSignalSet" (
	name TEXT NOT NULL,
	"SignalDefinitions_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalDefinitions_id") REFERENCES "SignalDefinitions" (id)
);CREATE INDEX "ix_DeviceTypeSignalSet_name" ON "DeviceTypeSignalSet" (name);
CREATE TABLE "GraphProjection" (
	id INTEGER NOT NULL,
	node_labels_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(node_labels_id) REFERENCES "NodeLabels" (id)
);CREATE INDEX "ix_GraphProjection_id" ON "GraphProjection" (id);
CREATE TABLE "KeyValuePair" (
	name TEXT NOT NULL,
	value TEXT,
	"JLabParams_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("JLabParams_id") REFERENCES "JLabParams" (id)
);CREATE INDEX "ix_KeyValuePair_name" ON "KeyValuePair" (name);
CREATE TABLE "NaradModel" (
	id INTEGER NOT NULL,
	narad_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(narad_id) REFERENCES "NaradConfig" (id)
);CREATE INDEX "ix_NaradModel_id" ON "NaradModel" (id);
CREATE TABLE "SignalBinding" (
	name TEXT NOT NULL,
	epics_suffix TEXT,
	description TEXT,
	"SignalDefinitions_id" INTEGER,
	"DeviceTypeSignalSet_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalDefinitions_id") REFERENCES "SignalDefinitions" (id),
	FOREIGN KEY("DeviceTypeSignalSet_name") REFERENCES "DeviceTypeSignalSet" (name)
);CREATE INDEX "ix_SignalBinding_name" ON "SignalBinding" (name);
CREATE TABLE "ControlProfileFamily" (
	name TEXT NOT NULL,
	kind TEXT,
	description TEXT,
	"CapabilityLayer_id" INTEGER,
	graph_projection_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("CapabilityLayer_id") REFERENCES "CapabilityLayer" (id),
	FOREIGN KEY(graph_projection_id) REFERENCES "GraphProjection" (id)
);CREATE INDEX "ix_ControlProfileFamily_name" ON "ControlProfileFamily" (name);
CREATE TABLE "GraphProjection_relationships" (
	"GraphProjection_id" INTEGER,
	relationships VARCHAR(28),
	PRIMARY KEY ("GraphProjection_id", relationships),
	FOREIGN KEY("GraphProjection_id") REFERENCES "GraphProjection" (id)
);CREATE INDEX "ix_GraphProjection_relationships_GraphProjection_id" ON "GraphProjection_relationships" ("GraphProjection_id");CREATE INDEX "ix_GraphProjection_relationships_relationships" ON "GraphProjection_relationships" (relationships);
CREATE TABLE "Capability" (
	name TEXT NOT NULL,
	description TEXT,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_Capability_name" ON "Capability" (name);
CREATE TABLE "CapabilityProfile" (
	name TEXT NOT NULL,
	kind TEXT,
	description TEXT,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_CapabilityProfile_name" ON "CapabilityProfile" (name);
CREATE TABLE "Beamline" (
	name TEXT NOT NULL,
	kind TEXT,
	"NaradModel_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id)
);CREATE INDEX "ix_Beamline_name" ON "Beamline" (name);
CREATE TABLE "TypeSpecificCapability" (
	id TEXT NOT NULL,
	capability_class TEXT,
	description TEXT,
	"CapabilityProfile_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name)
);CREATE INDEX "ix_TypeSpecificCapability_id" ON "TypeSpecificCapability" (id);
CREATE TABLE "ElementNaradRef" (
	id INTEGER NOT NULL,
	capability_profile_family TEXT,
	capability_profile TEXT,
	magnet_semantics_id INTEGER,
	instrument_semantics_id INTEGER,
	cavity_semantics_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(capability_profile_family) REFERENCES "ControlProfileFamily" (name),
	FOREIGN KEY(capability_profile) REFERENCES "CapabilityProfile" (name),
	FOREIGN KEY(magnet_semantics_id) REFERENCES "ElementSemantics" (id),
	FOREIGN KEY(instrument_semantics_id) REFERENCES "ElementSemantics" (id),
	FOREIGN KEY(cavity_semantics_id) REFERENCES "ElementSemantics" (id)
);CREATE INDEX "ix_ElementNaradRef_id" ON "ElementNaradRef" (id);
CREATE TABLE "CapabilityProfile_inherits_shared_capabilities" (
	"CapabilityProfile_name" TEXT,
	inherits_shared_capabilities TEXT,
	PRIMARY KEY ("CapabilityProfile_name", inherits_shared_capabilities),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name)
);CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_inherits_shared_capabilities" ON "CapabilityProfile_inherits_shared_capabilities" (inherits_shared_capabilities);CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_CapabilityProfile_name" ON "CapabilityProfile_inherits_shared_capabilities" ("CapabilityProfile_name");
CREATE TABLE "ElementSemantics_shared_capabilities" (
	"ElementSemantics_id" INTEGER,
	shared_capabilities_name TEXT,
	PRIMARY KEY ("ElementSemantics_id", shared_capabilities_name),
	FOREIGN KEY("ElementSemantics_id") REFERENCES "ElementSemantics" (id),
	FOREIGN KEY(shared_capabilities_name) REFERENCES "Capability" (name)
);CREATE INDEX "ix_ElementSemantics_shared_capabilities_ElementSemantics_id" ON "ElementSemantics_shared_capabilities" ("ElementSemantics_id");CREATE INDEX "ix_ElementSemantics_shared_capabilities_shared_capabilities_name" ON "ElementSemantics_shared_capabilities" (shared_capabilities_name);
CREATE TABLE "Signal" (
	name TEXT NOT NULL,
	role TEXT,
	data_type VARCHAR(16),
	units TEXT,
	description TEXT,
	"Capability_name" TEXT,
	"TypeSpecificCapability_id" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Capability_name") REFERENCES "Capability" (name),
	FOREIGN KEY("TypeSpecificCapability_id") REFERENCES "TypeSpecificCapability" (id)
);CREATE INDEX "ix_Signal_name" ON "Signal" (name);
CREATE TABLE "BeamlineElement" (
	name TEXT NOT NULL,
	kind VARCHAR(10),
	length FLOAT,
	"NaradModel_id" INTEGER,
	"RFP_id" INTEGER,
	"BendP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"SolenoidP_id" INTEGER,
	narad_id INTEGER,
	"JLabP_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParams" (id),
	FOREIGN KEY("BendP_id") REFERENCES "BendParams" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParams" (id),
	FOREIGN KEY("SolenoidP_id") REFERENCES "SolenoidParams" (id),
	FOREIGN KEY(narad_id) REFERENCES "ElementNaradRef" (id),
	FOREIGN KEY("JLabP_id") REFERENCES "JLabParams" (id)
);CREATE INDEX "ix_BeamlineElement_name" ON "BeamlineElement" (name);
CREATE TABLE "PVBinding" (
	name TEXT NOT NULL,
	facility TEXT,
	control_system TEXT,
	pv TEXT,
	"ElementNaradRef_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("ElementNaradRef_id") REFERENCES "ElementNaradRef" (id)
);CREATE INDEX "ix_PVBinding_name" ON "PVBinding" (name);
CREATE TABLE "ElementSemantics_type_specific_capabilities" (
	"ElementSemantics_id" INTEGER,
	type_specific_capabilities_id TEXT,
	PRIMARY KEY ("ElementSemantics_id", type_specific_capabilities_id),
	FOREIGN KEY("ElementSemantics_id") REFERENCES "ElementSemantics" (id),
	FOREIGN KEY(type_specific_capabilities_id) REFERENCES "TypeSpecificCapability" (id)
);CREATE INDEX "ix_ElementSemantics_type_specific_capabilities_type_specific_capabilities_id" ON "ElementSemantics_type_specific_capabilities" (type_specific_capabilities_id);CREATE INDEX "ix_ElementSemantics_type_specific_capabilities_ElementSemantics_id" ON "ElementSemantics_type_specific_capabilities" ("ElementSemantics_id");
CREATE TABLE "Beamline_line" (
	"Beamline_name" TEXT,
	line_name TEXT,
	PRIMARY KEY ("Beamline_name", line_name),
	FOREIGN KEY("Beamline_name") REFERENCES "Beamline" (name),
	FOREIGN KEY(line_name) REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_Beamline_line_Beamline_name" ON "Beamline_line" ("Beamline_name");CREATE INDEX "ix_Beamline_line_line_name" ON "Beamline_line" (line_name);

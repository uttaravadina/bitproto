# Code generated by bitproto. DO NOT EDIT.


"""
Proto drone describes the structure of the drone.
"""


import json
from dataclasses import dataclass, field
from typing import ClassVar, Dict, List

from bitprotolib import bp


Timestamp = int # 64bit

def bp_processor_Timestamp() -> bp.Processor:
    return bp.AliasProcessor(bp.Int(64))

def bp_default_factory_Timestamp() -> Timestamp:
    return 0


TernaryInt32 = List[int] # 96bit

def bp_processor_TernaryInt32() -> bp.Processor:
    return bp.AliasProcessor(bp.Array(False, 3, bp.Int(32)))

def bp_default_factory_TernaryInt32() -> TernaryInt32:
    return [0 for _ in range(3)]


DroneStatus = int # 3bit
DRONE_STATUS_UNKNOWN: DroneStatus = 0
DRONE_STATUS_STANDBY: DroneStatus = 1
DRONE_STATUS_RISING: DroneStatus = 2
DRONE_STATUS_LANDING: DroneStatus = 3
DRONE_STATUS_FLYING: DroneStatus = 4

_DRONESTATUS_VALUE_TO_NAME_MAP: Dict[DroneStatus, str] = {
    0: "DRONE_STATUS_UNKNOWN",
    1: "DRONE_STATUS_STANDBY",
    2: "DRONE_STATUS_RISING",
    3: "DRONE_STATUS_LANDING",
    4: "DRONE_STATUS_FLYING",
}

def bp_processor_DroneStatus() -> bp.Processor:
    return bp.EnumProcessor(bp.Uint(3))


PropellerStatus = int # 2bit
PROPELLER_STATUS_UNKNOWN: PropellerStatus = 0
PROPELLER_STATUS_IDLE: PropellerStatus = 1
PROPELLER_STATUS_ROTATING: PropellerStatus = 2

_PROPELLERSTATUS_VALUE_TO_NAME_MAP: Dict[PropellerStatus, str] = {
    0: "PROPELLER_STATUS_UNKNOWN",
    1: "PROPELLER_STATUS_IDLE",
    2: "PROPELLER_STATUS_ROTATING",
}

def bp_processor_PropellerStatus() -> bp.Processor:
    return bp.EnumProcessor(bp.Uint(2))


RotatingDirection = int # 2bit
ROTATING_DIRECTION_UNKNOWN: RotatingDirection = 0
ROTATING_DIRECTION_CLOCK_WISE: RotatingDirection = 1
ROTATING_DIRECTION_ANTI_CLOCK_WISE: RotatingDirection = 2

_ROTATINGDIRECTION_VALUE_TO_NAME_MAP: Dict[RotatingDirection, str] = {
    0: "ROTATING_DIRECTION_UNKNOWN",
    1: "ROTATING_DIRECTION_CLOCK_WISE",
    2: "ROTATING_DIRECTION_ANTI_CLOCK_WISE",
}

def bp_processor_RotatingDirection() -> bp.Processor:
    return bp.EnumProcessor(bp.Uint(2))


PowerStatus = int # 2bit
POWER_STATUS_UNKNOWN: PowerStatus = 0
POWER_STATUS_OFF: PowerStatus = 1
POWER_STATUS_ON: PowerStatus = 2

_POWERSTATUS_VALUE_TO_NAME_MAP: Dict[PowerStatus, str] = {
    0: "POWER_STATUS_UNKNOWN",
    1: "POWER_STATUS_OFF",
    2: "POWER_STATUS_ON",
}

def bp_processor_PowerStatus() -> bp.Processor:
    return bp.EnumProcessor(bp.Uint(2))


LandingGearStatus = int # 2bit
LANDING_GEAR_STATUS_UNKNOWN: LandingGearStatus = 0
LANDING_GEAR_STATUS_UNFOLDED: LandingGearStatus = 1
LANDING_GEAR_STATUS_FOLDED: LandingGearStatus = 2

_LANDINGGEARSTATUS_VALUE_TO_NAME_MAP: Dict[LandingGearStatus, str] = {
    0: "LANDING_GEAR_STATUS_UNKNOWN",
    1: "LANDING_GEAR_STATUS_UNFOLDED",
    2: "LANDING_GEAR_STATUS_FOLDED",
}

def bp_processor_LandingGearStatus() -> bp.Processor:
    return bp.EnumProcessor(bp.Uint(2))


@dataclass
class Propeller(bp.MessageBase):
    # Number of bytes to serialize class Propeller
    BYTES_LENGTH: ClassVar[int] = 2

    id: int = 0 # 8bit
    status: PropellerStatus = 0 # 2bit
    direction: RotatingDirection = 0 # 2bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp.Uint(8)),
            bp.MessageFieldProcessor(2, bp_processor_PropellerStatus()),
            bp.MessageFieldProcessor(3, bp_processor_RotatingDirection()),
        ]
        return bp.MessageProcessor(False, 12, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.id |= (int(b) << lshift)
        if di.field_number == 2:
            self.status |= (PropellerStatus(b) << lshift)
        if di.field_number == 3:
            self.direction |= (RotatingDirection(b) << lshift)
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.id >> rshift) & 255
        if di.field_number == 2:
            return (self.status >> rshift) & 255
        if di.field_number == 3:
            return (self.direction >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Power(bp.MessageBase):
    # Number of bytes to serialize class Power
    BYTES_LENGTH: ClassVar[int] = 2

    battery: int = 0 # 8bit
    status: PowerStatus = 0 # 2bit
    is_charging: bool = False # 1bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp.Uint(8)),
            bp.MessageFieldProcessor(2, bp_processor_PowerStatus()),
            bp.MessageFieldProcessor(3, bp.Bool()),
        ]
        return bp.MessageProcessor(False, 11, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.battery |= (int(b) << lshift)
        if di.field_number == 2:
            self.status |= (PowerStatus(b) << lshift)
        if di.field_number == 3:
            self.is_charging = bool(b)
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.battery >> rshift) & 255
        if di.field_number == 2:
            return (self.status >> rshift) & 255
        if di.field_number == 3:
            return (int(self.is_charging) >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Network(bp.MessageBase):
    # Number of bytes to serialize class Network
    BYTES_LENGTH: ClassVar[int] = 9

    # Degree of signal, between 1~10.
    signal: int = 0 # 4bit
    # The timestamp of the last time received heartbeat packet.
    heartbeat_at: Timestamp = field(default_factory=bp_default_factory_Timestamp) # 64bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp.Uint(4)),
            bp.MessageFieldProcessor(2, bp_processor_Timestamp()),
        ]
        return bp.MessageProcessor(False, 68, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.signal |= (int(b) << lshift)
        if di.field_number == 2:
            self.heartbeat_at |= bp.int64((int(b) << lshift))
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.signal >> rshift) & 255
        if di.field_number == 2:
            return (self.heartbeat_at >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class LandingGear(bp.MessageBase):
    # Number of bytes to serialize class LandingGear
    BYTES_LENGTH: ClassVar[int] = 1

    status: LandingGearStatus = 0 # 2bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp_processor_LandingGearStatus()),
        ]
        return bp.MessageProcessor(False, 2, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.status |= (LandingGearStatus(b) << lshift)
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.status >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Position(bp.MessageBase):
    # Number of bytes to serialize class Position
    BYTES_LENGTH: ClassVar[int] = 12

    latitude: int = 0 # 32bit
    longitude: int = 0 # 32bit
    altitude: int = 0 # 32bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp.Uint(32)),
            bp.MessageFieldProcessor(2, bp.Uint(32)),
            bp.MessageFieldProcessor(3, bp.Uint(32)),
        ]
        return bp.MessageProcessor(False, 96, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.latitude |= (int(b) << lshift)
        if di.field_number == 2:
            self.longitude |= (int(b) << lshift)
        if di.field_number == 3:
            self.altitude |= (int(b) << lshift)
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.latitude >> rshift) & 255
        if di.field_number == 2:
            return (self.longitude >> rshift) & 255
        if di.field_number == 3:
            return (self.altitude >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Pose(bp.MessageBase):
    """
    Pose in flight. https://en.wikipedia.org/wiki/Aircraft_principal_axes
    """
    # Number of bytes to serialize class Pose
    BYTES_LENGTH: ClassVar[int] = 12

    yaw: int = 0 # 32bit
    pitch: int = 0 # 32bit
    roll: int = 0 # 32bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp.Int(32)),
            bp.MessageFieldProcessor(2, bp.Int(32)),
            bp.MessageFieldProcessor(3, bp.Int(32)),
        ]
        return bp.MessageProcessor(False, 96, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.yaw |= bp.int32((int(b) << lshift))
        if di.field_number == 2:
            self.pitch |= bp.int32((int(b) << lshift))
        if di.field_number == 3:
            self.roll |= bp.int32((int(b) << lshift))
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.yaw >> rshift) & 255
        if di.field_number == 2:
            return (self.pitch >> rshift) & 255
        if di.field_number == 3:
            return (self.roll >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Flight(bp.MessageBase):
    # Number of bytes to serialize class Flight
    BYTES_LENGTH: ClassVar[int] = 36

    pose: Pose = field(default_factory=Pose) # 96bit
    # Velocity at X, Y, Z axis.
    velocity: TernaryInt32 = field(default_factory=bp_default_factory_TernaryInt32) # 96bit
    # Acceleration at X, Y, Z axis.
    acceleration: TernaryInt32 = field(default_factory=bp_default_factory_TernaryInt32) # 96bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, Pose().bp_processor()),
            bp.MessageFieldProcessor(2, bp_processor_TernaryInt32()),
            bp.MessageFieldProcessor(3, bp_processor_TernaryInt32()),
        ]
        return bp.MessageProcessor(False, 288, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 2:
            self.velocity[di.i(0)] |= bp.int32((int(b) << lshift))
        if di.field_number == 3:
            self.acceleration[di.i(0)] |= bp.int32((int(b) << lshift))
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 2:
            return (self.velocity[di.i(0)] >> rshift) & 255
        if di.field_number == 3:
            return (self.acceleration[di.i(0)] >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        if di.field_number == 1:
            return self.pose
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)


@dataclass
class Drone(bp.MessageBase):
    # Number of bytes to serialize class Drone
    BYTES_LENGTH: ClassVar[int] = 65

    status: DroneStatus = 0 # 3bit
    position: Position = field(default_factory=Position) # 96bit
    flight: Flight = field(default_factory=Flight) # 288bit
    propellers: List[Propeller] = field(default_factory=lambda: [Propeller() for _ in range(4)]) # 48bit
    power: Power = field(default_factory=Power) # 11bit
    network: Network = field(default_factory=Network) # 68bit
    landing_gear: LandingGear = field(default_factory=LandingGear) # 2bit

    def bp_processor(self) -> bp.Processor:
        field_processors: List[bp.Processor] = [
            bp.MessageFieldProcessor(1, bp_processor_DroneStatus()),
            bp.MessageFieldProcessor(2, Position().bp_processor()),
            bp.MessageFieldProcessor(3, Flight().bp_processor()),
            bp.MessageFieldProcessor(4, bp.Array(False, 4, Propeller().bp_processor())),
            bp.MessageFieldProcessor(5, Power().bp_processor()),
            bp.MessageFieldProcessor(6, Network().bp_processor()),
            bp.MessageFieldProcessor(7, LandingGear().bp_processor()),
        ]
        return bp.MessageProcessor(False, 516, field_processors)

    def bp_set_byte(self, di: bp.DataIndexer, lshift: int, b: bp.byte) -> None:
        if di.field_number == 1:
            self.status |= (DroneStatus(b) << lshift)
        return

    def bp_get_byte(self, di: bp.DataIndexer, rshift: int) -> bp.byte:
        if di.field_number == 1:
            return (self.status >> rshift) & 255
        return bp.byte(0)  # Won't reached

    def bp_get_accessor(self, di: bp.DataIndexer) -> bp.Accessor:
        if di.field_number == 2:
            return self.position
        if di.field_number == 3:
            return self.flight
        if di.field_number == 4:
            return self.propellers[di.i(0)]
        if di.field_number == 5:
            return self.power
        if di.field_number == 6:
            return self.network
        if di.field_number == 7:
            return self.landing_gear
        return bp.NilAccessor() # Won't reached

    def encode(self) -> bytearray:
        """
        Encode this object to bytearray.
        """
        s = bytearray(self.BYTES_LENGTH)
        ctx = bp.ProcessContext(True, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
        return ctx.s

    def decode(self, s: bytearray) -> None:
        """
        Decode given bytearray s to this object.
        :param s: A bytearray with length at least `BYTES_LENGTH`.
        """
        assert len(s) >= self.BYTES_LENGTH, bp.NotEnoughBytes()
        ctx = bp.ProcessContext(False, s)
        self.bp_processor().process(ctx, bp.NIL_DATA_INDEXER, self)
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class RadiusUnit(str, Enum):
    KM = 'KM'
    MILE = 'MILE'


class HotelSource(str, Enum):
    BEDBANK = 'BEDBANK'
    DIRECTCHAIN = 'DIRECTCHAIN'
    ALL = 'ALL'


class Amenity(str, Enum):
    SWIMMING_POOL = 'SWIMMING_POOL'
    SPA = 'SPA'
    FITNESS_CENTER = 'FITNESS_CENTER'
    AIR_CONDITIONING = 'AIR_CONDITIONING'
    RESTAURANT = 'RESTAURANT'
    PARKING = 'PARKING'
    PETS_ALLOWED = 'PETS_ALLOWED'
    AIRPORT_SHUTTLE = 'AIRPORT_SHUTTLE'
    BUSINESS_CENTER = 'BUSINESS_CENTER'
    DISABLED_FACILITIES = 'DISABLED_FACILITIES'
    WIFI = 'WIFI'
    MEETING_ROOMS = 'MEETING_ROOMS'
    NO_KID_ALLOWED = 'NO_KID_ALLOWED'
    TENNIS = 'TENNIS'
    GOLF = 'GOLF'
    KITCHEN = 'KITCHEN'
    ANIMAL_WATCHING = 'ANIMAL_WATCHING'
    BABY_SITTING = 'BABY-SITTING'
    BEACH = 'BEACH'
    CASINO = 'CASINO'
    JACUZZI = 'JACUZZI'
    SAUNA = 'SAUNA'
    SOLARIUM = 'SOLARIUM'
    MASSAGE = 'MASSAGE'
    VALET_PARKING = 'VALET_PARKING'
    BAR_OR_LOUNGE = 'BAR or LOUNGE'
    KIDS_WELCOME = 'KIDS_WELCOME'
    NO_PORN_FILMS = 'NO_PORN_FILMS'
    MINIBAR = 'MINIBAR'
    TELEVISION = 'TELEVISION'
    WIFI_IN_ROOM = 'WI-FI_IN_ROOM'
    ROOM_SERVICE = 'ROOM_SERVICE'
    GUARDED_PARKG = 'GUARDED_PARKG'
    SERV_SPEC_MENU = 'SERV_SPEC_MENU'


class Rating(str, Enum):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'


class HotelSearchRequest(BaseModel):
    city_code: str = Field(..., description="Destination city code (IATA)")
    radius: Optional[int] = Field(5, description="Search radius (default: 5)")
    radius_unit: Optional[RadiusUnit] = Field(RadiusUnit.KM, description="Radius unit (KM/MILE)")
    chain_codes: Optional[List[str]] = Field(None, description="Hotel chain codes (2-letter codes)")
    amenities: Optional[List[Amenity]] = Field(None, description="Hotel amenities filter")
    ratings: Optional[List[Rating]] = Field(None, description="Hotel star ratings")
    hotel_source: Optional[HotelSource] = Field(HotelSource.ALL, description="Hotel data source")


class HotelOfferRequest(BaseModel):
    hotel_ids: str = Field(..., description="Hotel ID (e.g., 'HLPAR266')")
    check_in_date: str = Field(..., description="YYYY-MM-DD")
    check_out_date: str = Field(..., description="YYYY-MM-DD")
    adults: int = Field(1, description="Number of adults")
    room_quantity: int = Field(1, description="Number of rooms")


class HotelOfferRequestParams(BaseModel):
    hotel_ids: List[str] = Field(..., description="Amadeus property codes (8 chars)")
    adults: int = Field(1, ge=1, le=9)
    check_in_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    check_out_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    country_of_residence: Optional[str] = Field(None, description="ISO 3166-1 code")
    room_quantity: int = Field(1, ge=1, le=9)
    price_range: Optional[str] = Field(None, example="200-300")
    currency: Optional[str] = Field(None, example="EUR")
    payment_policy: str = Field("NONE", description="Payment type filter")
    board_type: Optional[str] = Field(None, example="ROOM_ONLY")
    include_closed: bool = Field(False, description="Include sold-out hotels")
    best_rate_only: bool = Field(True, description="Return cheapest offer only")
    lang: str = Field("EN", description="ISO 639 language code")


class Guest(BaseModel):
    tid: int = Field(..., example=1, alias="tid")
    title: str = Field(..., example="MR", alias="title")
    firstName: str = Field(..., example="BOB", alias="firstName")
    lastName: str = Field(..., example="SMITH", alias="lastName")
    phone: str = Field(..., example="+33679278416", alias="phone")
    email: str = Field(..., example="bob.smith@email.com", alias="email")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class GuestReference(BaseModel):
    guestReference: str = Field(..., example="1", alias="guestReference")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class RoomAssociation(BaseModel):
    guestReferences: List[GuestReference] = Field(
        ...,
        example=[{"guestReference": "1"}],
        alias="guestReferences"
    )
    hotelOfferId: str = Field(..., example="94MRASSKRV", alias="hotelOfferId")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class PaymentCardInfo(BaseModel):
    vendorCode: str = Field(..., example="VI", alias="vendorCode")
    cardNumber: str = Field(..., example="4151289722471370", alias="cardNumber")
    expiryDate: str = Field(..., example="2026-08", alias="expiryDate")
    holderName: str = Field(..., example="BOB SMITH", alias="holderName")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class PaymentCard(BaseModel):
    paymentCardInfo: PaymentCardInfo = Field(..., alias="paymentCardInfo")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class Payment(BaseModel):
    method: str = Field(..., example="CREDIT_CARD", alias="method")
    paymentCard: PaymentCard = Field(..., alias="paymentCard")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class TravelAgentContact(BaseModel):
    email: str = Field(..., example="agent@example.com", alias="email")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class TravelAgent(BaseModel):
    contact: TravelAgentContact = Field(..., alias="contact")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class HotelOrderData(BaseModel):
    type: str = Field(default="hotel-order", alias="type")
    guests: List[Guest] = Field(..., alias="guests")
    travelAgent: TravelAgent = Field(..., alias="travelAgent")
    roomAssociations: List[RoomAssociation] = Field(..., alias="roomAssociations")
    payment: Payment = Field(..., alias="payment")
    remarks: Optional[str] = Field(None, alias="remarks")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class HotelBookingRequest(BaseModel):
    data: HotelOrderData = Field(..., alias="data")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True
        alias_generator = lambda s: s

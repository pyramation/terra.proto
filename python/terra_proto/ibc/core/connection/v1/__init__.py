# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/connection/v1/connection.proto, ibc/core/connection/v1/genesis.proto, ibc/core/connection/v1/query.proto, ibc/core/connection/v1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class State(betterproto.Enum):
    """
    State defines if a connection is in one of the following states: INIT,
    TRYOPEN, OPEN or UNINITIALIZED.
    """

    # Default State
    STATE_UNINITIALIZED_UNSPECIFIED = 0
    # A connection end has just started the opening handshake.
    STATE_INIT = 1
    # A connection end has acknowledged the handshake step on the counterparty
    # chain.
    STATE_TRYOPEN = 2
    # A connection end has completed the handshake.
    STATE_OPEN = 3


@dataclass(eq=False, repr=False)
class ConnectionEnd(betterproto.Message):
    """
    ConnectionEnd defines a stateful object on a chain connected to another
    separate one. NOTE: there must only be 2 defined ConnectionEnds to
    establish a connection between two chains.
    """

    # client associated with this connection.
    client_id: str = betterproto.string_field(1)
    # IBC version which can be utilised to determine encodings or protocols for
    # channels or packets utilising this connection.
    versions: List["Version"] = betterproto.message_field(2)
    # current state of the connection end.
    state: "State" = betterproto.enum_field(3)
    # counterparty chain associated with this connection.
    counterparty: "Counterparty" = betterproto.message_field(4)
    # delay period that must pass before a consensus state can be used for
    # packet-verification NOTE: delay period logic is only implemented by some
    # clients.
    delay_period: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class IdentifiedConnection(betterproto.Message):
    """
    IdentifiedConnection defines a connection with additional connection
    identifier field.
    """

    # connection identifier.
    id: str = betterproto.string_field(1)
    # client associated with this connection.
    client_id: str = betterproto.string_field(2)
    # IBC version which can be utilised to determine encodings or protocols for
    # channels or packets utilising this connection
    versions: List["Version"] = betterproto.message_field(3)
    # current state of the connection end.
    state: "State" = betterproto.enum_field(4)
    # counterparty chain associated with this connection.
    counterparty: "Counterparty" = betterproto.message_field(5)
    # delay period associated with this connection.
    delay_period: int = betterproto.uint64_field(6)


@dataclass(eq=False, repr=False)
class Counterparty(betterproto.Message):
    """
    Counterparty defines the counterparty chain associated with a connection
    end.
    """

    # identifies the client on the counterparty chain associated with a given
    # connection.
    client_id: str = betterproto.string_field(1)
    # identifies the connection end on the counterparty chain associated with a
    # given connection.
    connection_id: str = betterproto.string_field(2)
    # commitment merkle prefix of the counterparty chain.
    prefix: "__commitment_v1__.MerklePrefix" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ClientPaths(betterproto.Message):
    """ClientPaths define all the connection paths for a client state."""

    # list of connection paths
    paths: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ConnectionPaths(betterproto.Message):
    """
    ConnectionPaths define all the connection paths for a given client state.
    """

    # client state unique identifier
    client_id: str = betterproto.string_field(1)
    # list of connection paths
    paths: List[str] = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Version(betterproto.Message):
    """
    Version defines the versioning scheme used to negotiate the IBC verison in
    the connection handshake.
    """

    # unique version identifier
    identifier: str = betterproto.string_field(1)
    # list of features compatible with the specified identifier
    features: List[str] = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the set of Connection parameters."""

    # maximum expected time per block (in nanoseconds), used to enforce block
    # delay. This parameter should reflect the largest amount of time that the
    # chain might reasonably take to produce the next block under normal
    # operating conditions. A safe choice is 3-5x the expected time per block.
    max_expected_time_per_block: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc connection submodule's genesis state."""

    connections: List["IdentifiedConnection"] = betterproto.message_field(1)
    client_connection_paths: List["ConnectionPaths"] = betterproto.message_field(2)
    # the sequence for the next generated connection identifier
    next_connection_sequence: int = betterproto.uint64_field(3)
    params: "Params" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenInit(betterproto.Message):
    """
    MsgConnectionOpenInit defines the msg sent by an account on Chain A to
    initialize a connection with Chain B.
    """

    client_id: str = betterproto.string_field(1)
    counterparty: "Counterparty" = betterproto.message_field(2)
    version: "Version" = betterproto.message_field(3)
    delay_period: int = betterproto.uint64_field(4)
    signer: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenInitResponse(betterproto.Message):
    """
    MsgConnectionOpenInitResponse defines the Msg/ConnectionOpenInit response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenTry(betterproto.Message):
    """
    MsgConnectionOpenTry defines a msg sent by a Relayer to try to open a
    connection on Chain B.
    """

    client_id: str = betterproto.string_field(1)
    # in the case of crossing hello's, when both chains call OpenInit, we need
    # the connection identifier of the previous connection in state INIT
    previous_connection_id: str = betterproto.string_field(2)
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)
    counterparty: "Counterparty" = betterproto.message_field(4)
    delay_period: int = betterproto.uint64_field(5)
    counterparty_versions: List["Version"] = betterproto.message_field(6)
    proof_height: "__client_v1__.Height" = betterproto.message_field(7)
    # proof of the initialization the connection on Chain A: `UNITIALIZED ->
    # INIT`
    proof_init: bytes = betterproto.bytes_field(8)
    # proof of client state included in message
    proof_client: bytes = betterproto.bytes_field(9)
    # proof of client consensus state
    proof_consensus: bytes = betterproto.bytes_field(10)
    consensus_height: "__client_v1__.Height" = betterproto.message_field(11)
    signer: str = betterproto.string_field(12)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenTryResponse(betterproto.Message):
    """
    MsgConnectionOpenTryResponse defines the Msg/ConnectionOpenTry response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenAck(betterproto.Message):
    """
    MsgConnectionOpenAck defines a msg sent by a Relayer to Chain A to
    acknowledge the change of connection state to TRYOPEN on Chain B.
    """

    connection_id: str = betterproto.string_field(1)
    counterparty_connection_id: str = betterproto.string_field(2)
    version: "Version" = betterproto.message_field(3)
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(4)
    proof_height: "__client_v1__.Height" = betterproto.message_field(5)
    # proof of the initialization the connection on Chain B: `UNITIALIZED ->
    # TRYOPEN`
    proof_try: bytes = betterproto.bytes_field(6)
    # proof of client state included in message
    proof_client: bytes = betterproto.bytes_field(7)
    # proof of client consensus state
    proof_consensus: bytes = betterproto.bytes_field(8)
    consensus_height: "__client_v1__.Height" = betterproto.message_field(9)
    signer: str = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenAckResponse(betterproto.Message):
    """
    MsgConnectionOpenAckResponse defines the Msg/ConnectionOpenAck response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenConfirm(betterproto.Message):
    """
    MsgConnectionOpenConfirm defines a msg sent by a Relayer to Chain B to
    acknowledge the change of connection state to OPEN on Chain A.
    """

    connection_id: str = betterproto.string_field(1)
    # proof for the change of the connection state on Chain A: `INIT -> OPEN`
    proof_ack: bytes = betterproto.bytes_field(2)
    proof_height: "__client_v1__.Height" = betterproto.message_field(3)
    signer: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenConfirmResponse(betterproto.Message):
    """
    MsgConnectionOpenConfirmResponse defines the Msg/ConnectionOpenConfirm
    response type.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryConnectionRequest(betterproto.Message):
    """
    QueryConnectionRequest is the request type for the Query/Connection RPC
    method
    """

    # connection unique identifier
    connection_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryConnectionResponse(betterproto.Message):
    """
    QueryConnectionResponse is the response type for the Query/Connection RPC
    method. Besides the connection end, it includes a proof and the height from
    which the proof was retrieved.
    """

    # connection associated with the request identifier
    connection: "ConnectionEnd" = betterproto.message_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # height at which the proof was retrieved
    proof_height: "__client_v1__.Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryConnectionsRequest(betterproto.Message):
    """
    QueryConnectionsRequest is the request type for the Query/Connections RPC
    method
    """

    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryConnectionsResponse(betterproto.Message):
    """
    QueryConnectionsResponse is the response type for the Query/Connections RPC
    method.
    """

    # list of stored connections of the chain.
    connections: List["IdentifiedConnection"] = betterproto.message_field(1)
    # pagination response
    pagination: "____cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    # query block height
    height: "__client_v1__.Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryClientConnectionsRequest(betterproto.Message):
    """
    QueryClientConnectionsRequest is the request type for the
    Query/ClientConnections RPC method
    """

    # client identifier associated with a connection
    client_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryClientConnectionsResponse(betterproto.Message):
    """
    QueryClientConnectionsResponse is the response type for the
    Query/ClientConnections RPC method
    """

    # slice of all the connection paths associated with a client.
    connection_paths: List[str] = betterproto.string_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # height at which the proof was generated
    proof_height: "__client_v1__.Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryConnectionClientStateRequest(betterproto.Message):
    """
    QueryConnectionClientStateRequest is the request type for the
    Query/ConnectionClientState RPC method
    """

    # connection identifier
    connection_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryConnectionClientStateResponse(betterproto.Message):
    """
    QueryConnectionClientStateResponse is the response type for the
    Query/ConnectionClientState RPC method
    """

    # client state associated with the channel
    identified_client_state: "__client_v1__.IdentifiedClientState" = (
        betterproto.message_field(1)
    )
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # height at which the proof was retrieved
    proof_height: "__client_v1__.Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryConnectionConsensusStateRequest(betterproto.Message):
    """
    QueryConnectionConsensusStateRequest is the request type for the
    Query/ConnectionConsensusState RPC method
    """

    # connection identifier
    connection_id: str = betterproto.string_field(1)
    revision_number: int = betterproto.uint64_field(2)
    revision_height: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class QueryConnectionConsensusStateResponse(betterproto.Message):
    """
    QueryConnectionConsensusStateResponse is the response type for the
    Query/ConnectionConsensusState RPC method
    """

    # consensus state associated with the channel
    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        1
    )
    # client ID associated with the consensus state
    client_id: str = betterproto.string_field(2)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(3)
    # height at which the proof was retrieved
    proof_height: "__client_v1__.Height" = betterproto.message_field(4)


class MsgStub(betterproto.ServiceStub):
    async def connection_open_init(
        self,
        *,
        client_id: str = "",
        counterparty: "Counterparty" = None,
        version: "Version" = None,
        delay_period: int = 0,
        signer: str = "",
    ) -> "MsgConnectionOpenInitResponse":

        request = MsgConnectionOpenInit()
        request.client_id = client_id
        if counterparty is not None:
            request.counterparty = counterparty
        if version is not None:
            request.version = version
        request.delay_period = delay_period
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenInit",
            request,
            MsgConnectionOpenInitResponse,
        )

    async def connection_open_try(
        self,
        *,
        client_id: str = "",
        previous_connection_id: str = "",
        client_state: "betterproto_lib_google_protobuf.Any" = None,
        counterparty: "Counterparty" = None,
        delay_period: int = 0,
        counterparty_versions: Optional[List["Version"]] = None,
        proof_height: "__client_v1__.Height" = None,
        proof_init: bytes = b"",
        proof_client: bytes = b"",
        proof_consensus: bytes = b"",
        consensus_height: "__client_v1__.Height" = None,
        signer: str = "",
    ) -> "MsgConnectionOpenTryResponse":
        counterparty_versions = counterparty_versions or []

        request = MsgConnectionOpenTry()
        request.client_id = client_id
        request.previous_connection_id = previous_connection_id
        if client_state is not None:
            request.client_state = client_state
        if counterparty is not None:
            request.counterparty = counterparty
        request.delay_period = delay_period
        if counterparty_versions is not None:
            request.counterparty_versions = counterparty_versions
        if proof_height is not None:
            request.proof_height = proof_height
        request.proof_init = proof_init
        request.proof_client = proof_client
        request.proof_consensus = proof_consensus
        if consensus_height is not None:
            request.consensus_height = consensus_height
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenTry",
            request,
            MsgConnectionOpenTryResponse,
        )

    async def connection_open_ack(
        self,
        *,
        connection_id: str = "",
        counterparty_connection_id: str = "",
        version: "Version" = None,
        client_state: "betterproto_lib_google_protobuf.Any" = None,
        proof_height: "__client_v1__.Height" = None,
        proof_try: bytes = b"",
        proof_client: bytes = b"",
        proof_consensus: bytes = b"",
        consensus_height: "__client_v1__.Height" = None,
        signer: str = "",
    ) -> "MsgConnectionOpenAckResponse":

        request = MsgConnectionOpenAck()
        request.connection_id = connection_id
        request.counterparty_connection_id = counterparty_connection_id
        if version is not None:
            request.version = version
        if client_state is not None:
            request.client_state = client_state
        if proof_height is not None:
            request.proof_height = proof_height
        request.proof_try = proof_try
        request.proof_client = proof_client
        request.proof_consensus = proof_consensus
        if consensus_height is not None:
            request.consensus_height = consensus_height
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenAck",
            request,
            MsgConnectionOpenAckResponse,
        )

    async def connection_open_confirm(
        self,
        *,
        connection_id: str = "",
        proof_ack: bytes = b"",
        proof_height: "__client_v1__.Height" = None,
        signer: str = "",
    ) -> "MsgConnectionOpenConfirmResponse":

        request = MsgConnectionOpenConfirm()
        request.connection_id = connection_id
        request.proof_ack = proof_ack
        if proof_height is not None:
            request.proof_height = proof_height
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenConfirm",
            request,
            MsgConnectionOpenConfirmResponse,
        )


class QueryStub(betterproto.ServiceStub):
    async def connection(self, *, connection_id: str = "") -> "QueryConnectionResponse":

        request = QueryConnectionRequest()
        request.connection_id = connection_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connection", request, QueryConnectionResponse
        )

    async def connections(
        self, *, pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryConnectionsResponse":

        request = QueryConnectionsRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connections",
            request,
            QueryConnectionsResponse,
        )

    async def client_connections(
        self, *, client_id: str = ""
    ) -> "QueryClientConnectionsResponse":

        request = QueryClientConnectionsRequest()
        request.client_id = client_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ClientConnections",
            request,
            QueryClientConnectionsResponse,
        )

    async def connection_client_state(
        self, *, connection_id: str = ""
    ) -> "QueryConnectionClientStateResponse":

        request = QueryConnectionClientStateRequest()
        request.connection_id = connection_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionClientState",
            request,
            QueryConnectionClientStateResponse,
        )

    async def connection_consensus_state(
        self,
        *,
        connection_id: str = "",
        revision_number: int = 0,
        revision_height: int = 0,
    ) -> "QueryConnectionConsensusStateResponse":

        request = QueryConnectionConsensusStateRequest()
        request.connection_id = connection_id
        request.revision_number = revision_number
        request.revision_height = revision_height

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionConsensusState",
            request,
            QueryConnectionConsensusStateResponse,
        )


class MsgBase(ServiceBase):
    async def connection_open_init(
        self,
        client_id: str,
        counterparty: "Counterparty",
        version: "Version",
        delay_period: int,
        signer: str,
    ) -> "MsgConnectionOpenInitResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_try(
        self,
        client_id: str,
        previous_connection_id: str,
        client_state: "betterproto_lib_google_protobuf.Any",
        counterparty: "Counterparty",
        delay_period: int,
        counterparty_versions: Optional[List["Version"]],
        proof_height: "__client_v1__.Height",
        proof_init: bytes,
        proof_client: bytes,
        proof_consensus: bytes,
        consensus_height: "__client_v1__.Height",
        signer: str,
    ) -> "MsgConnectionOpenTryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_ack(
        self,
        connection_id: str,
        counterparty_connection_id: str,
        version: "Version",
        client_state: "betterproto_lib_google_protobuf.Any",
        proof_height: "__client_v1__.Height",
        proof_try: bytes,
        proof_client: bytes,
        proof_consensus: bytes,
        consensus_height: "__client_v1__.Height",
        signer: str,
    ) -> "MsgConnectionOpenAckResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_confirm(
        self,
        connection_id: str,
        proof_ack: bytes,
        proof_height: "__client_v1__.Height",
        signer: str,
    ) -> "MsgConnectionOpenConfirmResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_connection_open_init(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "counterparty": request.counterparty,
            "version": request.version,
            "delay_period": request.delay_period,
            "signer": request.signer,
        }

        response = await self.connection_open_init(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connection_open_try(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "previous_connection_id": request.previous_connection_id,
            "client_state": request.client_state,
            "counterparty": request.counterparty,
            "delay_period": request.delay_period,
            "counterparty_versions": request.counterparty_versions,
            "proof_height": request.proof_height,
            "proof_init": request.proof_init,
            "proof_client": request.proof_client,
            "proof_consensus": request.proof_consensus,
            "consensus_height": request.consensus_height,
            "signer": request.signer,
        }

        response = await self.connection_open_try(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connection_open_ack(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connection_id": request.connection_id,
            "counterparty_connection_id": request.counterparty_connection_id,
            "version": request.version,
            "client_state": request.client_state,
            "proof_height": request.proof_height,
            "proof_try": request.proof_try,
            "proof_client": request.proof_client,
            "proof_consensus": request.proof_consensus,
            "consensus_height": request.consensus_height,
            "signer": request.signer,
        }

        response = await self.connection_open_ack(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connection_open_confirm(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connection_id": request.connection_id,
            "proof_ack": request.proof_ack,
            "proof_height": request.proof_height,
            "signer": request.signer,
        }

        response = await self.connection_open_confirm(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.connection.v1.Msg/ConnectionOpenInit": grpclib.const.Handler(
                self.__rpc_connection_open_init,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenInit,
                MsgConnectionOpenInitResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenTry": grpclib.const.Handler(
                self.__rpc_connection_open_try,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenTry,
                MsgConnectionOpenTryResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenAck": grpclib.const.Handler(
                self.__rpc_connection_open_ack,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenAck,
                MsgConnectionOpenAckResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenConfirm": grpclib.const.Handler(
                self.__rpc_connection_open_confirm,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenConfirm,
                MsgConnectionOpenConfirmResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def connection(self, connection_id: str) -> "QueryConnectionResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connections(
        self, pagination: "____cosmos_base_query_v1_beta1__.PageRequest"
    ) -> "QueryConnectionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_connections(
        self, client_id: str
    ) -> "QueryClientConnectionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_client_state(
        self, connection_id: str
    ) -> "QueryConnectionClientStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_consensus_state(
        self, connection_id: str, revision_number: int, revision_height: int
    ) -> "QueryConnectionConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_connection(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connection_id": request.connection_id,
        }

        response = await self.connection(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connections(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.connections(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_client_connections(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
        }

        response = await self.client_connections(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connection_client_state(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connection_id": request.connection_id,
        }

        response = await self.connection_client_state(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connection_consensus_state(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connection_id": request.connection_id,
            "revision_number": request.revision_number,
            "revision_height": request.revision_height,
        }

        response = await self.connection_consensus_state(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.connection.v1.Query/Connection": grpclib.const.Handler(
                self.__rpc_connection,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionRequest,
                QueryConnectionResponse,
            ),
            "/ibc.core.connection.v1.Query/Connections": grpclib.const.Handler(
                self.__rpc_connections,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionsRequest,
                QueryConnectionsResponse,
            ),
            "/ibc.core.connection.v1.Query/ClientConnections": grpclib.const.Handler(
                self.__rpc_client_connections,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientConnectionsRequest,
                QueryClientConnectionsResponse,
            ),
            "/ibc.core.connection.v1.Query/ConnectionClientState": grpclib.const.Handler(
                self.__rpc_connection_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionClientStateRequest,
                QueryConnectionClientStateResponse,
            ),
            "/ibc.core.connection.v1.Query/ConnectionConsensusState": grpclib.const.Handler(
                self.__rpc_connection_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionConsensusStateRequest,
                QueryConnectionConsensusStateResponse,
            ),
        }


from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from ...client import v1 as __client_v1__
from ...commitment import v1 as __commitment_v1__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

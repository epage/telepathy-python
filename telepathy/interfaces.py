# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005 Collabora Limited
# Copyright (C) 2005 Nokia Corporation
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

CONN_MGR_INTERFACE = 'org.freedesktop.Telepathy.ConnectionManager'

CONN_INTERFACE = 'org.freedesktop.Telepathy.Connection'

CONN_INTERFACE_ALIASING = CONN_INTERFACE + '.Interface.Aliasing'
CONN_INTERFACE_AVATARS = CONN_INTERFACE + '.Interface.Avatars'
CONN_INTERFACE_CAPABILITIES = CONN_INTERFACE + '.Interface.Capabilities'
CONN_INTERFACE_CONTACT_INFO = CONN_INTERFACE + '.Interface.ContactInfo'
CONN_INTERFACE_FORWARDING = CONN_INTERFACE + '.Interface.Forwarding'
CONN_INTERFACE_PRESENCE = CONN_INTERFACE + '.Interface.Presence'
CONN_INTERFACE_PRIVACY = CONN_INTERFACE + '.Interface.Privacy'
CONN_INTERFACE_RENAMING = CONN_INTERFACE + '.Interface.Renaming'

CHANNEL_INTERFACE = 'org.freedesktop.Telepathy.Channel'
CHANNEL_TYPE_CONTACT_LIST = 'org.freedesktop.Telepathy.Channel.Type.ContactList'
CHANNEL_TYPE_CONTACT_SEARCH = 'org.freedesktop.Telepathy.Channel.Type.ContactSearch'
CHANNEL_TYPE_TEXT = 'org.freedesktop.Telepathy.Channel.Type.Text'
CHANNEL_TYPE_ROOM_LIST = 'org.freedesktop.Telepathy.Channel.Type.RoomList'
CHANNEL_TYPE_STREAMED_MEDIA = 'org.freedesktop.Telepathy.Channel.Type.StreamedMedia'

CHANNEL_INTERFACE_DTMF = 'org.freedesktop.Telepathy.Channel.Interface.DTMF'
CHANNEL_INTERFACE_GROUP = 'org.freedesktop.Telepathy.Channel.Interface.Group'
CHANNEL_INTERFACE_HOLD = 'org.freedesktop.Telepathy.Channel.Interface.Hold'
CHANNEL_INTERFACE_MEDIA_SIGNALLING = 'org.freedesktop.Telepathy.Channel.Interface.MediaSignalling'
CHANNEL_INTERFACE_PASSWORD = 'org.freedesktop.Telepathy.Channel.Interface.Password'
CHANNEL_INTERFACE_TRANSFER = 'org.freedesktop.Telepathy.Channel.Interface.Transfer'

MEDIA_SESSION_HANDLER = 'org.freedesktop.Telepathy.Media.SessionHandler'
MEDIA_STREAM_HANDLER = 'org.freedesktop.Telepathy.Media.StreamHandler'

PROPERTIES_INTERFACE = 'org.freedesktop.Telepathy.Properties'

CHANNEL_HANDLER_INTERFACE = 'org.freedesktop.Telepathy.ChannelHandler'

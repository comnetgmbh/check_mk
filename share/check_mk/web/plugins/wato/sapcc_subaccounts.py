#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Copyright (C) 2019  Frank Fegert (fra.nospam.nk@gmx.de)
#
# WATO plugin for the parametrization of the threshold values
# used by the "sapcc_subaccounts" Check_MK check script.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
register_check_parameters(
    subgroup_applications,
    "sapcc_subaccounts",
    _("SAP Cloud Connector Subaccounts"),
    Dictionary(
        elements = [
            ( "app_conn_levels",
              Tuple(
                  help = _("The number of application connections for a SAP Cloud Connector subaccount."),
                  title =_("CURRENTLY NOT USED! Number of application connections"),
                  elements = [
                      Integer(title = _("Warning at or below"), unit = _("connections"), default_value = 0),
                      Integer(title = _("Critical at or below"), unit = _("connections"), default_value = 0),
                      Integer(title = _("Warning at or above"), unit = _("connections"), default_value = 30),
                      Integer(title = _("Critical at or above"), unit = _("connections"), default_value = 40),
                  ])
            ),
            ( "conn_num_levels",
              Tuple(
                  help = _("The number of tunnel connections for a SAP Cloud Connector subaccount."),
                  title =_("Number of tunnel connections"),
                  elements = [
                      Integer(title = _("Warning at or above"), unit = _("connections"), default_value = 30),
                      Integer(title = _("Critical at or above"), unit = _("connections"), default_value = 40),
                      Integer(title = _("Warning at or below"), unit = _("connections"), default_value = 0),
                      Integer(title = _("Critical at or below"), unit = _("connections"), default_value = 0),
                  ])
            ),
            ( "conn_time_levels",
              Tuple(
                  help = _("The amount of time a tunnel connections is active on a SAP Cloud Connector subaccount."),
                  title =_("Connection time of tunnel connections"),
                  elements = [
                      Age(title = _("Warning at or above"), default_value = 284012568),
                      Age(title = _("Critical at or above"), default_value = 315569520),
                      Age(title = _("Warning at or below"), default_value = 0),
                      Age(title = _("Critical at or below"), default_value = 0),
                  ])
            ),
        ]
    ),
    TextAscii(
        title = _("Subaccount ID"),
    ),
    "dict"
)

#
## EOF

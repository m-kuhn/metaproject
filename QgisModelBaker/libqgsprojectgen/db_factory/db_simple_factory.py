# -*- coding: utf-8 -*-
"""
/***************************************************************************
    begin                :    08/04/19
    git sha              :    :%H$
    copyright            :    (C) 2019 by Yesid Polania
    email                :    yesidpol.3@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from .pg_factory import PgFactory
from .gpkg_factory import GpkgFactory
from QgisModelBaker.libili2db.globals import DbIliMode, displayDbIliMode


class DbSimpleFactory:

    def create_factory(self, ili_mode):
        if not ili_mode:
            return None

        result = None

        if ili_mode & DbIliMode.pg:
            result = PgFactory()
        elif ili_mode & DbIliMode.gpkg:
            result = GpkgFactory()

        return result

    def get_db_list(self, is_schema_import=False):
        ili = []
        result = [DbIliMode.pg, DbIliMode.gpkg]

        if is_schema_import:
            for item in result:
                print(item)
                ili += [item | DbIliMode.ili]

            result = ili + result

        return result

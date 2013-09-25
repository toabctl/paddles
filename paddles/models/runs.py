import os
from hashlib import sha1
from sqlalchemy import Column, Integer, String, Unicode, Boolean
from sqlalchemy.orm import synonym
from sqlalchemy.orm.exc import DetachedInstanceError
from paddles.models import Base
from paddles.models.types import JSONType


class Run(Base):

    __tablename__ = 'runs'
    id = Column(Integer, primary_key=True)
    archive_path = Column(String(256))
    description = Column(String(128))
    duration = Column(Integer)
    email = Column(String(64))
    flavor = Column(String(64))
    job_id = Column(String(32))
    kernel = Column(JSONType())
    last_in_suite = Column(Boolean())
    machine_type = Column(String(32))
    mon.a_kernel_sha1 = Column(String(128))
    mon.b_kernel_sha1 = Column(String(128))
    name = Column(String(128))
    nuke_on_error = Column(Boolean())
    os_type = Column(String(16))
    overrides = Column(JSONType())
    owner = Column(String(64))
    pid = Column(String(16))
    roles = Column(JSONType())
    success = Column(Boolean())
    targets = Column(JSONType())
    tasks = Column(JSONType())
    teuthology_branch = Column(String(16))
    verbose = Column(Boolean())

    def __repr__(self):
        try:
            return '<Run %r>' % self.username
        except DetachedInstanceError:
            return '<Run detached>'

    def __json__(self):
        return dict(
            name = self.name,
            email = self.email,
            archive_path = self.archive_path,
            description = self.description,
            duration = self.duration,
            flavor = self.flavor,
            job_id = self.job_id,
            kernel = self.kernel,
            last_in_suite = self.last_in_suite,
            machine_type = self.machine_type,
            mon_a_kernel_sha1 = self.mon.a_kernel_sha1,
            mon_b_kernel_sha1 = self.mon.b_kernel_sha1,
            nuke_on_error = self.nuke_on_error,
            os_type = self.os_type,
            overrides = self.overrides,
            owner = self.owner,
            pid = self.pid,
            roles = self.roles,
            success = self.success,
            targets = self.targets,
            tasks = self.tasks,
            teuthology_branch = self.teuthology_branch,
            verbose = self.verbose,
        )

package com.SoftDevTimeSheet.entity;

import org.springframework.security.core.authority.SimpleGrantedAuthority;
import java.util.Set;
import java.util.stream.Collectors;

public enum Role {
    WORKER(Set.of(Permission.WORKER_SELF_REPORT_MAKE,Permission.WORKER_SELF_HOURS_ADD)),
    DIRECTOR(Set.of(Permission.DIRECTOR_ADD_HOURS_TO_WORKER,
            Permission.DIRECTOR_MAKE_REPORT_FOR_WORKER,
            Permission.DIRECTOR_MAKE_REPORT_FOR_ALL,
            Permission.DIRECTOR_ADD_NEW_WORKER,
            Permission.DIRECTOR_REMOVE_WORKER
    )),

    FREELANCER(Set.of(Permission.FREELANCER_SELF_REPORT_MAKE,Permission.FREELANCER_SELF_HOURS_ADD));

    Role(Set<Permission> permissions) {
        this.permissions = permissions;
    }

    public Set<Permission> getPermissions() {
        return permissions;
    }

    private  final Set<Permission> permissions;

    public Set<SimpleGrantedAuthority> getAuthorities(){
        return  getPermissions().stream().map(permission -> new SimpleGrantedAuthority(permission.getPermission()))
                .collect(Collectors.toSet());
    }
}
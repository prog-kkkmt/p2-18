package com.SoftDevTimeSheet.repository;

import com.SoftDevTimeSheet.entity.Worker;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<Worker, Long> {
    Optional<Worker> findByName(String name);
}

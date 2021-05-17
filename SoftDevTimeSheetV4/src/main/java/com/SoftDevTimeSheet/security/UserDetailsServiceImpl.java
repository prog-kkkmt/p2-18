package com.SoftDevTimeSheet.security;

import com.SoftDevTimeSheet.entity.Worker;
import com.SoftDevTimeSheet.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service("userDetailsServiceImpl")
public class UserDetailsServiceImpl implements UserDetailsService {

    private  final UserRepository userRepository;

    @Autowired
    public UserDetailsServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String name) throws UsernameNotFoundException {
        Worker worker = userRepository.findByName(name).orElseThrow(() -> new UsernameNotFoundException("User doesn't exist"));
        return  SecurityUser.fromUser(worker);
    }
}

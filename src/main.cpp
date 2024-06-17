#include <fmt/core.h>

#include <utxo/common.hpp>

int main(int argc, char** argv) {

    std::string_view const path = "/home/fernando/dev/utxo-experiments/src";

    size_t total_inputs;
    size_t total_outputs;
    size_t partial_inputs;
    size_t partial_outputs;

    process(path,
        [&](auto const& tx_hashes, auto&& txs) {
            fmt::print("txs.size() = {}\n", txs.size());
            fmt::print("do something with txs\n");
        },
        [&]() {
            fmt::print("post processing\n");
        },
        total_inputs, total_outputs, partial_inputs, partial_outputs);

    fmt::print("Total inputs:    {}\n", total_inputs);
    fmt::print("Total outputs:   {}\n", total_outputs);
    fmt::print("Partial Inputs:  {:7}\n", partial_inputs);
    fmt::print("Partial Outputs: {:7}\n", partial_outputs);

    return 0;
}
